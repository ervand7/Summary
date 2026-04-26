package main

import (
	"fmt"
	"sync"
	"time"
)

func work(wg *sync.WaitGroup, jobs <-chan int, workerID int) {
	defer wg.Done()
	for job := range jobs {
		time.Sleep(time.Second) // simulate hard work
		fmt.Printf("worker %d processes job %d\n", workerID, job)
	}
}

func main() {
	var (
		wg           sync.WaitGroup
		workersCount = 10
		jobsCount    = 100
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
