package main

import (
	"fmt"
	"math/rand"
	"runtime"
	"sync"
	"time"
)

type poolWorkFn[Input any, Result any] func(input Input) Result

func poolWork[Input any, Result any](
	size int,
	work poolWorkFn[Input, Result],
) (chan Input, func()) {
	var wg sync.WaitGroup
	wg.Add(size)
	ch := make(chan Input)
	for i := 0; i < size; i++ {
		go func() {
			defer wg.Done()
			for input := range ch {
				result := work(input)
				fmt.Println("pollWork :", result)
			}
		}()
	}
	cancel := func() {
		close(ch)
		wg.Wait()
	}
	return ch, cancel
}

func main() {
	size := runtime.GOMAXPROCS(0)
	pwf := func(input int) string {
		time.Sleep(time.Duration(rand.Intn(200)) * time.Millisecond)
		return fmt.Sprintf("%d : received", input)
	}
	ch, cancel := poolWork(size, pwf)
	defer cancel()
	for i := 0; i < 4; i++ {
		ch <- i
	}
}
