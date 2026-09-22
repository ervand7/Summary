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
 - if multiple goroutines request the same key simultaneously:
	 - underlying fetch must execute only once
	 - all callers receive same result
 - different keys may execute concurrently
 - support context cancellation
 - thread-safe
 - no goroutine leaks
 - failed requests must be removable for future retries
*/

type call struct {
	done  chan struct{}
	value string
	err   error
}

type RequestGroup struct {
	requests map[string]*call
	mu       sync.Mutex
}

func NewRequestGroup() *RequestGroup {
	return &RequestGroup{
		requests: make(map[string]*call),
	}
}

func (g *RequestGroup) Do(
	ctx context.Context,
	key string,
	fn func(context.Context) (string, error),
) (string, error) {
	if key == "" {
		return "", errors.New("empty key")
	}

	if fn == nil {
		return "", errors.New("nil function")
	}

	g.mu.Lock()
	if c, ok := g.requests[key]; ok {
		g.mu.Unlock()

		select {
		case <-ctx.Done():
			return "", ctx.Err()
		case <-c.done:
			return c.value, c.err
		}
	}

	c := &call{done: make(chan struct{})}
	g.requests[key] = c
	g.mu.Unlock()

	c.value, c.err = fn(ctx)

	g.mu.Lock()
	delete(g.requests, key)
	close(c.done)
	g.mu.Unlock()

	return c.value, c.err
}

func main() {
	g := NewRequestGroup()

	fn := func(ctx context.Context) (string, error) {
		fmt.Println("REAL API CALL STARTED")

		select {
		case <-time.After(2 * time.Second):
			fmt.Println("REAL API CALL FINISHED")
			return "data-from-api", nil

		case <-ctx.Done():
			return "", ctx.Err()
		}
	}

	// same key -> only ONE real execution should happen
	for i := 0; i < 5; i++ {
		go func(id int) {
			res, err := g.Do(context.Background(), "users", fn)
			fmt.Printf("[users] goroutine=%d result=%s err=%v\n", id, res, err)
		}(i)
	}

	// different key -> separate execution
	go func() {
		res, err := g.Do(context.Background(), "orders", fn)
		fmt.Printf("[orders] result=%s err=%v\n", res, err)
	}()

	time.Sleep(5 * time.Second)

	fmt.Println("SECOND ROUND")

	// should execute again after first completed
	for i := 0; i < 3; i++ {
		go func(id int) {
			res, err := g.Do(context.Background(), "users", fn)
			fmt.Printf("[second users] goroutine=%d result=%s err=%v\n", id, res, err)
		}(i)
	}

	time.Sleep(5 * time.Second)
}
