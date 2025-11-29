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
		time.Sleep(1300 * time.Millisecond)
		cancel()
	}()

	runJob2(ctx)
}

func runJob2(ctx context.Context) {
	fmt.Println("Job started")

	timer := time.NewTimer(500 * time.Millisecond)

	for step := 1; step <= 5; step++ {
		select {
		case <-ctx.Done():
			fmt.Println("Job cancelled:", ctx.Err())
			return

		case <-timer.C:
			fmt.Println("Step", step, "completed")
			timer.Reset(500 * time.Millisecond)
		}
	}

	fmt.Println("Job finished successfully")
}
