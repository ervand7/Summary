package main

import (
	"fmt"
	"sync"
	"time"
)

func funOut(wg *sync.WaitGroup, in <-chan int, out chan<- int, workerID int) {
	defer wg.Done()
	for job := range in {
		fmt.Printf("worker %d processes job %d\n", workerID, job)
		time.Sleep(time.Second) //  simulate hard work
		out <- job * job
	}
}

func main() {
	var (
		wg           sync.WaitGroup
		in           = make(chan int)
		out          = make(chan int)
		workersCount = 10
		jobsCount    = 100
	)

	for i := 0; i < workersCount; i++ {
		wg.Add(1)
		go funOut(&wg, in, out, i)
	}

	// fanIn
	go func() {
		for i := 0; i < jobsCount; i++ {
			in <- i
		}
		close(in)
	}()

	go func() {
		wg.Wait()
		close(out)
	}()

	for processedItem := range out {
		fmt.Printf("got %d\n", processedItem)
	}
}
