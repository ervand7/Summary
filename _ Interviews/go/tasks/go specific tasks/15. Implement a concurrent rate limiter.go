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

 - allow at most N requests per interval
 - multiple goroutines may call Allow()
 - blocked callers wait for next available token
 - support context cancellation while waiting
 - thread-safe
 - no goroutine leaks
 - graceful shutdown
*/

var ErrRateLimiterIsClosed = errors.New("rate limiter is closed")

type RateLimiter struct {
	isClosed bool
	mu       sync.Mutex
	wg       sync.WaitGroup
	tokens   chan struct{}
	limiter  *time.Ticker
	limit    int
	stopCh   chan struct{}
}

func NewRateLimiter(
	limit int,
	interval time.Duration,
) *RateLimiter {
	if limit == 0 {
		limit = 1
	}
	if interval == 0 {
		interval = 1
	}

	r := &RateLimiter{
		tokens:  make(chan struct{}, limit),
		stopCh:  make(chan struct{}),
		limiter: time.NewTicker(interval),
		limit:   limit,
	}

	r.wg.Add(1)
	go r.run()

	return r
}

func (r *RateLimiter) Allow(ctx context.Context) error {
	/*
		Requirements:
		- allow at most limit requests per interval
		- wait if no tokens available
		- respect context cancellation
		- thread-safe
	*/
	r.mu.Lock()
	if r.isClosed {
		r.mu.Unlock()
		return ErrRateLimiterIsClosed
	}
	r.mu.Unlock()

	select {
	case <-ctx.Done():
		return ctx.Err()
	case _, ok := <-r.tokens:
		if !ok {
			return ErrRateLimiterIsClosed
		}
		return nil
	}
}

func (r *RateLimiter) Close() {
	r.mu.Lock()
	if r.isClosed {
		r.mu.Unlock()
		return
	}

	r.isClosed = true
	close(r.stopCh)
	r.mu.Unlock()

	r.wg.Wait()

	close(r.tokens)
}

func (r *RateLimiter) run() {
	defer r.wg.Done()
	defer r.limiter.Stop()

	for {
		select {
		case <-r.stopCh:
			return

		case <-r.limiter.C:
			for i := 0; i < r.limit; i++ {
				select {
				case <-r.stopCh:
					return
				case r.tokens <- struct{}{}:
				default:
					// token bucket already full
				}
			}
		}
	}
}

func main() {
	limiter := NewRateLimiter(2, time.Second)

	var wg sync.WaitGroup

	for i := 0; i < 10; i++ {
		wg.Add(1)

		go func(id int) {
			defer wg.Done()

			ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
			defer cancel()

			err := limiter.Allow(ctx)
			if err != nil {
				fmt.Println("worker", id, "error:", err)
				return
			}

			fmt.Println("worker", id, "allowed at", time.Now().Format("15:04:05"))
		}(i)
	}

	wg.Wait()

	limiter.Close()
}
