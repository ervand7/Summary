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
	mid := processor(in)
	consumer(mid)
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
	// Requirements:
	// 1. Read from in
	// 2. Process with time.Sleep(20ms)
	// 3. Write to out
	// 4. Close out correctly

	var (
		workersCount = 10
		out          = make(chan int)
		wg           sync.WaitGroup
	)

	for i := 0; i < workersCount; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for val := range in {
				time.Sleep(time.Second)
				out <- val * val
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
	for i := range ch {
		fmt.Printf("received %d\n", i)
	}
}
