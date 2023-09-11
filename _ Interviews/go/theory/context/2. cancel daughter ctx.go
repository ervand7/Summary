package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

/*
Программа зависнет, так как отмена дочернего контекста не аффектит
на родительский контекст.
*/

func some(ctx context.Context, wg *sync.WaitGroup) {
	defer wg.Done()
	i := 0
	for {
		select {
		case <-ctx.Done():
			fmt.Println("first: daughter1 context was canceled")
			return
		default:
			fmt.Println(i)
		}
		i++
	}
}

func main() {
	wg := &sync.WaitGroup{}
	parentCtx, parentCancel := context.WithCancel(context.Background())
	defer parentCancel()
	daughterCtx, daughterCancel := context.WithCancel(parentCtx)
	_ = daughterCtx
	defer daughterCancel()

	wg.Add(1)
	go some(parentCtx, wg)

	time.AfterFunc(20*time.Millisecond, daughterCancel)
	wg.Wait()
}
