package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

// Goal:
// Write a worker-pool that transforms input values into output values using transform().
// Stop processing immediately when context is cancelled.
// Question:
// Implement the function parallelMap().

func main() {
	in := make(chan int, 50)
	out := make(chan int, 50)

	ctx, cancel := context.WithTimeout(context.Background(), 150*time.Millisecond)
	defer cancel()

	// producer
	go func() {
		for i := 1; i <= 10; i++ {
			in <- i
		}
		close(in)
	}()

	parallelMap(ctx, 3, in, out)

	for v := range out {
		fmt.Println("out:", v)
	}
}

func parallelMap(ctx context.Context, workers int, in <-chan int, out chan<- int) {
	var wg sync.WaitGroup
	wg.Add(workers)

	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()

			for {
				select {
				case <-ctx.Done():
					return
				case v, ok := <-in:
					if !ok {
						return
					}

					result := transform(v)

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

func transform(x int) int {
	time.Sleep(50 * time.Millisecond)
	return x * 10
}
