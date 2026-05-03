package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

// You have a list of logs that need to be processed concurrently using a pool of workers.

/*
📌 Requirements
Start exactly workers goroutines (worker pool).
Each log must be processed exactly once.
If any log processing returns an error:
 - stop sending new logs to workers
 - cancel the context for all workers
 - return that error
Logs that are already being processed are allowed to finish.
No goroutine leaks.
If ctx is canceled from outside → stop processing and return ctx.Err().
If workers <= 0 → return error.
If logs is empty → return nil.
*/

type LogEntry struct {
	ID      string
	UserID  string
	Message string
}

type Processor interface {
	Process(ctx context.Context, log LogEntry) error
}

var (
	ErrInvalidWorkersCount = errors.New("workers count should be positive")
)

func ProcessLogs(
	ctx context.Context,
	logs []LogEntry,
	processor Processor,
	workers int,
) error {
	if workers <= 0 {
		return ErrInvalidWorkersCount
	}

	if len(logs) == 0 {
		return nil
	}

	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	logsCh := make(chan LogEntry)
	errCh := make(chan error, 1)

	var wg sync.WaitGroup

	for i := 0; i < workers; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()

			for log := range logsCh {
				if err := processor.Process(ctx, log); err != nil {
					select {
					case errCh <- err:
						cancel()
					default:
					}
					return
				}
			}
		}()
	}

	go func() {
		defer close(logsCh)

		for _, log := range logs {
			select {
			case logsCh <- log:
			case <-ctx.Done():
				return
			}
		}
	}()

	doneCh := make(chan struct{})

	go func() {
		wg.Wait()
		close(doneCh)
	}()

	select {
	case <-doneCh:
		return nil

	case err := <-errCh:
		cancel()
		<-doneCh
		return err

	case <-ctx.Done():
		<-doneCh
		return ctx.Err()
	}
}

type mockProcessor struct {
	delay  time.Duration
	failID string
}

func (m mockProcessor) Process(ctx context.Context, log LogEntry) error {
	select {
	case <-time.After(m.delay):
		fmt.Println("processed:", log.ID)

		if log.ID == m.failID {
			return fmt.Errorf("failed to process log %s", log.ID)
		}

		return nil

	case <-ctx.Done():
		return ctx.Err()
	}
}

func main() {
	logs := []LogEntry{
		{ID: "log-1", UserID: "user-1", Message: "login"},
		{ID: "log-2", UserID: "user-2", Message: "payment"},
		{ID: "log-3", UserID: "user-1", Message: "logout"},
		{ID: "log-4", UserID: "user-3", Message: "error"},
		{ID: "log-5", UserID: "user-2", Message: "refund"},
	}

	processor := mockProcessor{
		delay:  200 * time.Millisecond,
		failID: "log-4",
	}

	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	err := ProcessLogs(ctx, logs, processor, 3)
	if err != nil {
		fmt.Println("error:", err)
		return
	}

	fmt.Println("all logs processed successfully")
}
