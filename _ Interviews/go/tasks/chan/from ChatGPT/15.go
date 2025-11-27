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
		for i := 1; i <= 10; i++ {
			time.Sleep(30 * time.Millisecond)
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

	out := make(chan int)
	var wg sync.WaitGroup

	const workers = 3
	wg.Add(workers)

	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()
			for val := range in {
				out <- val
			}
			time.Sleep(time.Millisecond * 20)
		}()
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

func consumer(in <-chan int) {
	for v := range in {
		fmt.Println("consumed:", v)
	}
}
