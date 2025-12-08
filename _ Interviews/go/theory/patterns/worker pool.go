package main

import (
	"fmt"
	"sync"
	"time"
)

func work(wg *sync.WaitGroup, jobs <-chan int, i int) {
	defer wg.Done()
	for job := range jobs {
		fmt.Printf("job %d processes value %d\n", i, job)
		time.Sleep(time.Second)
	}
}

func main() {
	const workersCount = 3
	const jobsCount = 10

	jobs := make(chan int)
	var wg sync.WaitGroup

	for i := 0; i < workersCount; i++ {
		wg.Add(1)
		go work(&wg, jobs, i)
	}

	for j := 0; j < jobsCount; j++ {
		jobs <- j
	}
	close(jobs)

	wg.Wait()
}
