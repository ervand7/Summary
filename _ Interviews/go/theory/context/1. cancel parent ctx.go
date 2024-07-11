package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

/*
1) создали родительский контекст
2) создали 2 разных дочерних контекста
3) передали дочерние контексты в функции
4) через какое-то время отменили родительский контекст
5) горутины first и second перестали работать, так как их контексты получили
сигнал <-ctx.Done() возникший из-за отмены их общего родительского контекста

Обратите внимание, что здесь все defer cancel отрабатывают безопасно. То есть
defer parentCancel() отрабатывает без ошибок с учетом того, что родительский
контекст уже был ранее явно закрыт.
И defer дочерийКонтекст() отрабатывает также без ошибок с учетом того, что перед
этим был отменен родительский контекст.
*/

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
