package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

func first(ctx context.Context, wg *sync.WaitGroup) {
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

func second(ctx context.Context, wg *sync.WaitGroup) {
	defer wg.Done()
	i := 0
	for {
		select {
		case <-ctx.Done():
			fmt.Println("second: daughter2 context was canceled")
			return
		default:
			fmt.Println(i)
		}
		i--
	}
}

func main() {
	wg := &sync.WaitGroup{}
	parentCtx, parentCancel := context.WithCancel(context.Background())
	defer parentCancel()
	daughterCtx1, daughterCancel1 := context.WithCancel(parentCtx)
	defer daughterCancel1()
	daughterCtx2, daughterCancel2 := context.WithCancel(parentCtx)
	defer daughterCancel2()

	wg.Add(2)
	go first(daughterCtx1, wg)
	go second(daughterCtx2, wg)

	time.AfterFunc(20*time.Millisecond, parentCancel)
	wg.Wait()
}
