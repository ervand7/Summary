package main

import (
	"fmt"
	"sync"
	"time"
)

func work(wg *sync.WaitGroup, jobs <-chan int, workerID int) {
	defer wg.Done()
	for job := range jobs {
		fmt.Printf("worker %d processes job %d\n", workerID, job)
		time.Sleep(time.Second) // simulate hard work
	}
}

func main() {
	var (
		jobsCount    = 100
		workersCount = 10
		wg           sync.WaitGroup
		jobs         = make(chan int)
	)

	for i := 0; i < workersCount; i++ {
		wg.Add(1)
		go work(&wg, jobs, i)
	}

	for i := 0; i < jobsCount; i++ {
		jobs <- i
	}
	close(jobs)

	wg.Wait()
}
