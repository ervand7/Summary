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
 - multiple goroutines may call Execute
 - execute function only when breaker is closed
 - after N failures → open breaker
 - open breaker rejects requests immediately
 - after timeout → allow one test request (half-open)
 - if test succeeds → close breaker
 - if test fails → open again
 - thread-safe
 - support context cancellation
 - no goroutine leaks
*/

type CircuitBeakerState string

var (
	Open     CircuitBeakerState = "OPEN"
	Closed   CircuitBeakerState = "CLOSED"
	HalfOpen CircuitBeakerState = "HALF_OPEN"
)

var (
	ErrCircuitOpen = errors.New("circuit breaker open")
	ErrFnIsNil     = errors.New("fn can not be nil")
)

type CircuitBreaker struct {
	state        CircuitBeakerState
	maxFailures  int
	resetTimeout time.Duration
	mu           sync.Mutex
	failures     int
	timeToReset  time.Time
	testing      bool
}

func NewCircuitBreaker(
	maxFailures int,
	resetTimeout time.Duration,
) *CircuitBreaker {
	if maxFailures <= 0 {
		maxFailures = 1
	}

	if resetTimeout <= 0 {
		resetTimeout = time.Second
	}

	b := CircuitBreaker{
		state:        Closed,
		maxFailures:  maxFailures,
		resetTimeout: resetTimeout,
	}
	return &b
}

func (c *CircuitBreaker) Execute(
	ctx context.Context,
	fn func(context.Context) error,
) error {
	if fn == nil {
		return ErrFnIsNil
	}

	select {
	case <-ctx.Done():
		return ctx.Err()
	default:
	}

	c.mu.Lock()

	if c.state == Closed {
		c.mu.Unlock()

		err := fn(ctx)
		if err == nil {
			c.mu.Lock()
			c.failures = 0
			c.mu.Unlock()
			return nil
		}

		c.mu.Lock()
		c.failures++
		if c.failures < c.maxFailures {
			c.mu.Unlock()
			return err
		}

		c.state = Open
		c.failures = 0
		c.timeToReset = time.Now().Add(c.resetTimeout)
		c.mu.Unlock()
		return err
	}

	if c.state == Open {
		if time.Now().Before(c.timeToReset) {
			c.mu.Unlock()
			return ErrCircuitOpen
		}

		c.state = HalfOpen
	}

	if c.state == HalfOpen {
		if c.testing {
			c.mu.Unlock()
			return ErrCircuitOpen
		}

		c.testing = true
		c.mu.Unlock()

		err := fn(ctx)

		c.mu.Lock()
		defer c.mu.Unlock()

		c.testing = false

		if err != nil {
			c.state = Open
			c.timeToReset = time.Now().Add(c.resetTimeout)
			return err
		}

		c.state = Closed
		c.failures = 0
		return nil
	}

	c.mu.Unlock()
	return nil
}

func main() {
	cb := NewCircuitBreaker(
		3,
		3*time.Second,
	)

	fn := func(ctx context.Context) error {
		fmt.Println("calling service")

		time.Sleep(300 * time.Millisecond)

		return errors.New("service failed")
	}

	for i := 0; i < 5; i++ {
		err := cb.Execute(
			context.Background(),
			fn,
		)

		fmt.Println(
			"request",
			i,
			"err:",
			err,
		)
	}

	fmt.Println("waiting reset timeout")

	time.Sleep(4 * time.Second)

	err := cb.Execute(
		context.Background(),
		func(ctx context.Context) error {
			fmt.Println("test request")
			return nil
		},
	)

	fmt.Println("after reset:", err)
}
