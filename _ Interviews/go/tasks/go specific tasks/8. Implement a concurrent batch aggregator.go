package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

type event struct {
	ID int
}

func FlushBatch(ctx context.Context, batch []event) error {
	select {
	case <-time.After(200 * time.Millisecond):
		fmt.Printf("flushed batch size=%d\n", len(batch))

		if len(batch) > 4 {
			return errors.New("batch too large")
		}

		return nil

	case <-ctx.Done():
		return ctx.Err()
	}
}

func StartBatchProcessor(
	ctx context.Context,
	batchSize int,
	flushInterval time.Duration,
	maxConcurrentFlushes int,
	input <-chan event,
) error {
	if batchSize <= 0 {
		return errors.New("batch size should be positive")
	}
	if flushInterval <= 0 {
		return errors.New("flush interval should be positive")
	}
	if maxConcurrentFlushes <= 0 {
		return errors.New("max concurrent flushes should be positive")
	}

	ticker := time.NewTicker(flushInterval)
	defer ticker.Stop()

	var (
		wg       sync.WaitGroup
		once     sync.Once
		firstErr error
		sem      = make(chan struct{}, maxConcurrentFlushes)
		batch    = make([]event, 0, batchSize)
	)

	flush := func() {
		if len(batch) == 0 {
			return
		}

		b := batch
		batch = make([]event, 0, batchSize)

		sem <- struct{}{}
		wg.Add(1)

		go func() {
			defer wg.Done()
			defer func() { <-sem }()

			if err := FlushBatch(ctx, b); err != nil {
				once.Do(func() { firstErr = err })
			}
		}()
	}

loop:
	for {
		select {
		case <-ctx.Done():
			break loop

		case <-ticker.C:
			flush()

		case e, ok := <-input:
			if !ok {
				break loop
			}

			batch = append(batch, e)
			if len(batch) == batchSize {
				flush()
				ticker.Reset(flushInterval)
			}
		}
	}

	flush()
	wg.Wait()

	if firstErr != nil {
		return firstErr
	}
	return ctx.Err()
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	input := make(chan event)

	go func() {
		defer close(input)

		for i := 1; i <= 20; i++ {
			input <- event{ID: i}
			time.Sleep(50 * time.Millisecond)
		}
	}()

	err := StartBatchProcessor(
		ctx,
		3,
		500*time.Millisecond,
		2,
		input,
	)

	fmt.Println("processor stopped:", err)
}
