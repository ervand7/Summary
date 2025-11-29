package main

import (
	"context"
	"fmt"
	"time"
)

// What will be printed?

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	go func() {
		time.Sleep(1200 * time.Millisecond)
		cancel()
	}()

	runJob(ctx)
}

func runJob(ctx context.Context) {
	fmt.Println("Job started")

	for i := 1; i <= 5; i++ {
		select {
		case <-ctx.Done():
			fmt.Println("Job stopped:", ctx.Err())
			return
		case <-time.After(500 * time.Millisecond):
			fmt.Println("Step", i, "done")
		}
	}

	fmt.Println("Job finished successfully")
}
