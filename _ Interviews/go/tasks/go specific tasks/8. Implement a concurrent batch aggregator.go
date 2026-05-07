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
		mu       sync.Mutex
		batch    = make([]event, 0, batchSize)
		firstErr error
		sem      = make(chan struct{}, maxConcurrentFlushes)
	)

	flush := func(batchToFlush []event) {
		if len(batchToFlush) == 0 {
			return
		}

		batchCopy := append([]event(nil), batchToFlush...)

		wg.Add(1)
		go func() {
			defer wg.Done()

			sem <- struct{}{}
			defer func() { <-sem }()

			if err := FlushBatch(ctx, batchCopy); err != nil {
				mu.Lock()
				if firstErr == nil {
					firstErr = err
				}
				mu.Unlock()
			}
		}()
	}

	for {
		select {
		case <-ctx.Done():
			flush(batch)
			wg.Wait()

			if firstErr != nil {
				return firstErr
			}
			return ctx.Err()

		case <-ticker.C:
			flush(batch)
			batch = make([]event, 0, batchSize)

		case e, ok := <-input:
			if !ok {
				flush(batch)
				wg.Wait()

				if firstErr != nil {
					return firstErr
				}
				return nil
			}

			batch = append(batch, e)

			if len(batch) == batchSize {
				flush(batch)
				batch = make([]event, 0, batchSize)
			}
		}
	}
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
