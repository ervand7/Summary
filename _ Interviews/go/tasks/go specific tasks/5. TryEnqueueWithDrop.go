package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

/*
You are building a bounded in-memory queue for events.
When the queue is full → you must drop events instead of blocking.
*/

type Event struct {
	ID   string
	Data string
}

type Handler interface {
	Handle(ctx context.Context, e Event) error
}

func StartProcessor(
	ctx context.Context,
	handler Handler,
	queueSize int,
	workers int,
) (func(e Event) bool, error) {
	if queueSize <= 0 {
		return nil, errors.New("queue size must be positive")
	}

	if workers <= 0 {
		return nil, errors.New("workers count must be positive")
	}

	queue := make(chan Event, queueSize)

	var wg sync.WaitGroup

	for i := 0; i < workers; i++ {
		wg.Add(1)

		go func() {
			defer wg.Done()

			for {
				select {
				case <-ctx.Done():
					return

				case e, ok := <-queue:
					if !ok {
						return
					}
					if err := handler.Handle(ctx, e); err != nil {
						fmt.Println("handler error:", err)
					}
				}
			}
		}()
	}

	enqueue := func(e Event) bool {
		select {
		case <-ctx.Done():
			return false

		case queue <- e:
			return true

		default:
			return false
		}
	}

	return enqueue, nil
}

type mockHandler struct {
	delay time.Duration
}

func (m mockHandler) Handle(ctx context.Context, e Event) error {
	select {
	case <-time.After(m.delay):
		fmt.Println("handled:", e.ID)
		return nil
	case <-ctx.Done():
		return ctx.Err()
	}
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	handler := mockHandler{delay: 300 * time.Millisecond}

	enqueue, err := StartProcessor(ctx, handler, 2, 2)
	if err != nil {
		fmt.Println(err.Error())
		return
	}

	for i := 1; i <= 10; i++ {
		ok := enqueue(Event{
			ID:   fmt.Sprintf("event-%d", i),
			Data: "data",
		})

		if ok {
			fmt.Println("enqueued:", i)
		} else {
			fmt.Println("dropped:", i)
		}

		time.Sleep(50 * time.Millisecond)
	}

	time.Sleep(2 * time.Second)
}
