package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cancel := context.WithCancel(context.Background())
	time.AfterFunc(time.Millisecond, cancel)

	func(ctx context.Context) {
		for i := 0; i < 1000000; i++ {
			select {
			case <-ctx.Done():
				fmt.Println("Context was canceled")
				return
			default:
				fmt.Println(i)
			}
		}
	}(ctx)
}
