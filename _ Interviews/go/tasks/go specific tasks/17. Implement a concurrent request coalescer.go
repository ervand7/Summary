package main

import (
	"context"
	"errors"
	"fmt"
	"sync"
	"time"
)

/*
Requirements:

 - requests with same key must be grouped together
 - only one expensive operation per key may run concurrently
 - all waiting callers receive same result
 - different keys run independently
 - support timeout/cancellation
 - failed request should allow future retries
 - thread-safe
 - no goroutine leaks
*/

type res struct {
	val string
	err error
}

type Coalescer struct {
	requests map[string][]chan res
	mu       sync.Mutex
}

func NewCoalescer() *Coalescer {
	return &Coalescer{requests: make(map[string][]chan res)}
}

func (c *Coalescer) Do(
	ctx context.Context,
	key string,
	fn func(context.Context) (string, error),
) (string, error) {
	/*
		Requirements:
		- same key executes fn only once concurrently
		- concurrent callers wait for same result
		- different keys execute independently
		- failed requests removable for retry
		- respect context cancellation
		- thread-safe
	*/
	if key == "" {
		return "", errors.New("empty key")
	}
	if fn == nil {
		return "", errors.New("nil func")
	}

	c.mu.Lock()
	if _, ok := c.requests[key]; ok {
		ch := make(chan res, 1)
		c.requests[key] = append(c.requests[key], ch)
		c.mu.Unlock()

		select {
		case <-ctx.Done():
			return "", ctx.Err()
		case result := <-ch:
			return result.val, result.err
		}
	}

	c.requests[key] = make([]chan res, 0)
	c.mu.Unlock()

	result, err := fn(ctx)

	c.mu.Lock()
	channels, ok := c.requests[key]
	if !ok {
		c.mu.Unlock()
		return result, err
	}
	delete(c.requests, key)
	c.mu.Unlock()

	for _, ch := range channels {
		ch <- res{val: result, err: err}
	}

	return result, err
}

func main() {
	c := NewCoalescer()

	fn := func(ctx context.Context) (string, error) {
		fmt.Println("EXPENSIVE OPERATION STARTED")

		select {
		case <-time.After(2 * time.Second):
			fmt.Println("EXPENSIVE OPERATION FINISHED")
			return "result-data", nil

		case <-ctx.Done():
			return "", ctx.Err()
		}
	}

	var wg sync.WaitGroup

	for i := 0; i < 5; i++ {
		wg.Add(1)

		go func(id int) {
			defer wg.Done()

			res, err := c.Do(context.Background(), "users", fn)

			fmt.Println(
				"goroutine",
				id,
				"result:",
				res,
				"err:",
				err,
			)
		}(i)
	}

	wg.Wait()
}
