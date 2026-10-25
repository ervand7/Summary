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
	tokens     chan struct{}
	waitCh     chan struct{}
	shutdownCh chan struct{}
	once       sync.Once
}

func NewRateLimiter(limit int, interval time.Duration) *RateLimiter {
	if limit <= 0 {
		limit = 1
	}
	if interval <= 0 {
		interval = time.Nanosecond
	}

	r := &RateLimiter{
		tokens:     make(chan struct{}, limit),
		waitCh:     make(chan struct{}),
		shutdownCh: make(chan struct{}),
	}

	go func() {
		defer close(r.waitCh)

		ticker := time.NewTicker(interval)
		defer ticker.Stop()

		for {
			select {
			case <-r.shutdownCh:
				return
			case <-ticker.C:
				for range limit {
					select {
					case r.tokens <- struct{}{}:
					default:
					}
				}
			}
		}
	}()

	return r
}

func (r *RateLimiter) Allow(ctx context.Context) error {
	select {
	case <-r.shutdownCh:
		return ErrRateLimiterIsClosed
	default:
	}

	select {
	case <-r.shutdownCh:
		return ErrRateLimiterIsClosed
	case <-ctx.Done():
		return ctx.Err()
	case <-r.tokens:
		select {
		case <-r.shutdownCh:
			return ErrRateLimiterIsClosed
		default:
			return nil
		}
	}
}

func (r *RateLimiter) Close() {
	r.once.Do(func() {
		close(r.shutdownCh)
	})
	<-r.waitCh
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
