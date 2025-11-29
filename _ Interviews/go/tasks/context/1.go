package main

import (
	"context"
	"fmt"
	"time"
)

// What will be the output

func main() {
	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()

	time.Sleep(2950 * time.Millisecond)
	doDbRequest(ctx)
}

func doDbRequest(ctx context.Context) {
	newCtx, cancel := context.WithTimeout(ctx, 10*time.Second)
	defer cancel()

	timer := time.NewTimer(1 * time.Second)
	select {
	case <-newCtx.Done():
		fmt.Println("Timeout")
	case <-timer.C:
		fmt.Println("Request Done")
	}
}
