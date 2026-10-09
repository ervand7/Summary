package main

import (
	"fmt"
	"sync"
	"time"
)

/*
	Goal:
	Implement a 3-stage pipeline:
	generator → chan
	processor → chan
	consumer → prints
	Need:
	 - stages run in parallel
	 - but each stage must respect backpressure
	 - close channels properly
	no goroutine leaks
*/

func main() {
	in := generator()
	out := processor(in)
	consumer(out)
}

func generator() <-chan int {
	ch := make(chan int)

	go func() {
		defer close(ch)
		for i := 0; i < 100; i++ {
			ch <- i
		}
	}()

	return ch
}

func processor(in <-chan int) <-chan int {
	var (
		out     = make(chan int)
		wg      sync.WaitGroup
		workers = 10
	)

	for range workers {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for val := range in {
				out <- val
				time.Sleep(time.Second)
			}
		}()
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

func consumer(ch <-chan int) {
	for val := range ch {
		fmt.Printf("process value %d\n", val)
	}
}
