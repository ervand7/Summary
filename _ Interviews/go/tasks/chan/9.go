package main

import (
	"fmt"
	"sync"
	"time"
)

// Implement semaphore with many writers and single reader

func main() {
	var (
		wg           sync.WaitGroup
		workersCount = 10
		jobsCount    = 100
		semaphore    = make(chan struct{}, workersCount)
		jobs         = make(chan int)
	)

	// single reader
	go func() {
		for val := range jobs {
			fmt.Printf("got %d\n", val)
		}
	}()

	for i := 0; i < jobsCount; i++ {
		semaphore <- struct{}{}
		wg.Add(1)
		go func(item int) {
			defer wg.Done()
			defer func() { <-semaphore }()
			jobs <- item * item
			time.Sleep(time.Second)
		}(i)
	}

	wg.Wait()
	close(jobs)
}
