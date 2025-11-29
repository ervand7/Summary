package main

import (
	"context"
	"fmt"
	"sync"
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

	// Unlimited fast producer
	go func() {
		i := 1
		for {
			in <- i
			i++
			time.Sleep(50 * time.Millisecond) // fast producer
		}
	}()

	go rateLimitedProcess(ctx, in, out)

	// Consumer (just print)
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

	const workers = 5
	const rate = 3

	tokens := make(chan struct{}, rate)

	go func() {
		ticker := time.NewTicker(time.Second / rate)
		defer ticker.Stop()
		for {
			select {
			case <-ctx.Done():
				return
			case <-ticker.C:
				select {
				case tokens <- struct{}{}:
				default:
				}
			}
		}
	}()

	var wg sync.WaitGroup
	wg.Add(workers)

	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()

			for {
				select {
				case <-ctx.Done():
					return

				case task := <-in:
					select {
					case <-ctx.Done():
						return
					case <-tokens:
					}

					result := process(task)
					select {
					case <-ctx.Done():
						return
					case out <- result:
					}
				}
			}
		}()
	}

	go func() {
		wg.Wait()
		close(out)
	}()
}

func process(v int) int {
	// Simulate small work
	time.Sleep(20 * time.Millisecond)
	return v * 2
}
