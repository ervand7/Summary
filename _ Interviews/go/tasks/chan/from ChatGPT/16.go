package main

import (
	"context"
	"fmt"
	"time"
)

// Goal:
// Process incoming tasks, but at most 3 per second.
// Unlimited producer.
// Use rate limiter (token bucket or ticker).
// Worker pool (3–5 workers).
// Backpressure must be handled.
// Graceful shutdown when ctx is cancelled.

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()

	in := make(chan int, 100)
	out := make(chan int, 100)

	// unlimited producer
	go func() {
		defer close(in)
		for i := 1; ; i++ {
			select {
			case <-ctx.Done():
				return
			case in <- i:
				time.Sleep(50 * time.Millisecond)
			}
		}
	}()

	go rateLimitedProcess(ctx, in, out)

	for v := range out {
		fmt.Println("processed:", v)
	}
}

func rateLimitedProcess(ctx context.Context, in <-chan int, out chan<- int) {
	// Implement:
	// 1. A token bucket or ticker limiting to 3 ops / second
	// 2. Workers reading from `in`
	// 3. Workers wait for a rate limiter permit
	// 4. Stop when ctx cancels
	// 5. Close `out` correctly

	defer close(out)

	ticker := time.NewTicker(time.Second / 3) // 3 ops/sec
	defer ticker.Stop()

	for {
		select {
		case <-ctx.Done():
			return

		case task, ok := <-in:
			if !ok {
				return
			}

			<-ticker.C           // rate limit
			out <- process(task) // backpressure here
		}
	}
}

func process(v int) int {
	time.Sleep(20 * time.Millisecond)
	return v * 2
}
