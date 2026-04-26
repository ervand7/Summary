package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var (
		wg        sync.WaitGroup
		limit     = 10
		jobsCount = 100
		semaphore = make(chan struct{}, limit)
	)

	for i := 0; i < jobsCount; i++ {
		wg.Add(1)
		semaphore <- struct{}{}

		go func(jobID int) {
			defer wg.Done()
			defer func() { <-semaphore }()
			time.Sleep(time.Second) // simulate hard work
			fmt.Printf("job %d\n", jobID)
		}(i)
	}

	wg.Wait()
}
