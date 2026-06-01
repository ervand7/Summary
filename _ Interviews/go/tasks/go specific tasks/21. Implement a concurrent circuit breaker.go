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
	ErrCircuitOpen         = errors.New("circuit breaker open")
	ErrCircuitIsTerminated = errors.New("circuit breaker is stopped")
	ErrFnIsNil             = errors.New("fn can not be nil")
)

type CircuitBreaker struct {
	state        CircuitBeakerState
	maxFailures  int
	resetTimeout time.Duration
	mu           sync.RWMutex
	failures     int
	timeToReset  time.Time
	isTerminated bool
	once         sync.Once
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
	/*
		Requirements:
		- CLOSED:
		    execute all requests normally

		- OPEN:
		    reject immediately

		- after resetTimeout:
		    move to HALF_OPEN

		- HALF_OPEN:
		    allow only ONE request

		- success:
		    HALF_OPEN -> CLOSED

		- failure:
		    HALF_OPEN -> OPEN

		- thread-safe
		- respect ctx cancellation
	*/
	go c.once.Do(func() {
		fmt.Println("should be executed once")

		select {
		case <-ctx.Done():
			c.mu.Lock()
			c.isTerminated = true
			c.mu.Unlock()
			return
		}
	})

	if fn == nil {
		return ErrFnIsNil
	}

	c.mu.RLock()
	if c.isTerminated {
		c.mu.RUnlock()
		return ErrCircuitIsTerminated
	}

	if c.state == Closed {
		c.mu.RUnlock()

		err := fn(ctx)
		if err == nil {
			return nil
		}

		c.mu.Lock()
		c.failures++
		if c.failures != c.maxFailures {
			c.mu.Unlock()
			return nil
		}

		c.state = Open
		c.failures = 0
		c.timeToReset = time.Now().Add(c.resetTimeout)
		c.mu.Unlock()
		return err
	}

	if c.state == Open {
		c.mu.RUnlock()

		if time.Now().Before(c.timeToReset) {
			return ErrCircuitOpen
		}

		c.mu.Lock()
		c.state = HalfOpen
		err := fn(ctx)
		if err != nil {
			c.state = Open
			c.timeToReset = time.Now().Add(c.resetTimeout)
			c.mu.Unlock()
			return err
		}

		c.state = Closed
		c.mu.Unlock()
		return nil
	}

	c.mu.RUnlock()

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
