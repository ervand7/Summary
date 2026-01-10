package main

import (
	"fmt"
	"sync"
	"time"
)

// Implement semaphore with many writers and single reader

func main() {
	var (
		workersCount = 10
		jobsCount    = 100
		wg           sync.WaitGroup
		jobs         = make(chan int)
		semaphore    = make(chan struct{}, workersCount)
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
			time.Sleep(time.Second) // simulate hard work
		}(i)
	}

	go func() {
		wg.Wait()
		close(jobs)
	}()
}
