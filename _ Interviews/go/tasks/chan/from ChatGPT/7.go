package main

import (
	"context"
	"fmt"
	"time"
)

func fanOut(ctx context.Context, out chan<- int, channels ...<-chan int) {
	for _, ch := range channels {
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

	in1 := make(chan int)
	in2 := make(chan int)
	out := make(chan int)

	fanOut(ctx, out, in1, in2)

	// Writer #1
	go func() {
		for i := 0; i < 10; i++ {
			in1 <- i
			time.Sleep(100 * time.Millisecond)
		}
	}()

	// Writer #2
	go func() {
		for i := 0; i < 20; i++ {
			in2 <- i * 10
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
