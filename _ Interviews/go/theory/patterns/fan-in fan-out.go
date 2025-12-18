package main

import (
	"fmt"
	"sync"
	"time"
)

func fanOut(id int, wg *sync.WaitGroup, in <-chan int, out chan<- int) {
	defer wg.Done()
	for job := range in {
		fmt.Printf("worker %d processes value %d\n", id, job)
		time.Sleep(time.Second)
		out <- job * job
	}
}

func main() {
	const workersCount = 3
	const jobsCount = 10

	var (
		wg  sync.WaitGroup
		in  = make(chan int)
		out = make(chan int)
	)

	for i := 0; i < workersCount; i++ {
		wg.Add(1)
		go fanOut(i, &wg, in, out)
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	// fanIn
	go func() {
		for j := 0; j < jobsCount; j++ {
			in <- j
		}
		close(in)
	}()

	for i := range out {
		fmt.Printf("result %d\n", i)
	}
}
