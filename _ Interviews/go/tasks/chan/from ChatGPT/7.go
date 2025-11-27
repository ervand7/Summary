package main

import (
	"context"
	"fmt"
	"time"
)

// fanIn merges multiple input channels into a single output channel.
func fanIn(ctx context.Context, out chan<- int, channels ...<-chan int) {
	for _, ch := range channels {
		// Start a goroutine per input channel
		go func(c <-chan int) {
			for {
				select {
				case <-ctx.Done():
					return
				case v := <-c:
					out <- v
				}
			}
		}(ch)
	}
}

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	// Each writer has its own input channel
	src1 := make(chan int)
	src2 := make(chan int)
	out := make(chan int)

	// Merge multiple channels into one
	fanIn(ctx, out, src1, src2)

	// Writer #1
	go func() {
		for i := 0; i < 10; i++ {
			src1 <- i
			time.Sleep(100 * time.Millisecond)
		}
	}()

	// Writer #2
	go func() {
		for i := 0; i < 20; i++ {
			src2 <- i * 10
			time.Sleep(50 * time.Millisecond)
		}
	}()

	// Reader
	for {
		select {
		case <-ctx.Done():
			fmt.Println("Finishing: time elapsed")
			return
		case v := <-out:
			fmt.Println("read:", v)
		}
	}
}
