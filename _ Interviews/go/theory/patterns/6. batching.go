package main

import (
	"fmt"
	"time"
)

// Goal: collect many small requests → process them together as one batch.

func main() {
	jobs := make(chan int)

	// worker that batches
	go func() {
		batch := []int{}

		for {
			select {
			case job := <-jobs:
				batch = append(batch, job)

				if len(batch) >= 3 {
					fmt.Println("Process batch:", batch)
					batch = nil
				}

			case <-time.After(500 * time.Millisecond):
				if len(batch) > 0 {
					fmt.Println("Process batch (timeout):", batch)
					batch = nil
				}
			}
		}
	}()

	// send jobs quickly
	for i := 1; i <= 5; i++ {
		jobs <- i
		time.Sleep(100 * time.Millisecond)
	}

	time.Sleep(1 * time.Second)
}
