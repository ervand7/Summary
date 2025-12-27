package main

import (
	"fmt"
	"sync"
	"time"
)

func fanOut(wg *sync.WaitGroup, in <-chan int, out chan<- int, workerID int) {
	defer wg.Done()
	for val := range in {
		time.Sleep(time.Second)
		fmt.Printf("worker %d process val %d\n", workerID, val)
		out <- val * val
	}

}

func main() {
	var (
		wg           sync.WaitGroup
		in           = make(chan int)
		out          = make(chan int)
		workersCount = 3
		jobsCount    = 10
	)

	for i := 0; i < workersCount; i++ {
		wg.Add(1)
		go fanOut(&wg, in, out, i)
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	go func() {
		for i := 0; i < jobsCount; i++ {
			in <- i
		}
		close(in)
	}()

	for i := range out {
		fmt.Printf("received result %d\n", i)
	}

	fmt.Println("program finished")
}
