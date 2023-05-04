package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

func main() {
	wg := &sync.WaitGroup{}
	ctx, cancel := context.WithCancel(context.Background())

	wg.Add(1)
	go func(ctx context.Context, wg *sync.WaitGroup) {
		defer wg.Done()
		i := 0
		for {
			select {
			case <-ctx.Done():
				fmt.Println("Context was canceled")
				return
			default:
				fmt.Println(i)
			}
			i++
		}
	}(ctx, wg)

	time.AfterFunc(20*time.Millisecond, cancel)
	wg.Wait()
}
