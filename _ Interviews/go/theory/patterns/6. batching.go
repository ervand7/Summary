package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	jobs := make(chan int)
	batchSize := 3
	batch := make([]int, 0, batchSize)

	wg.Add(1)
	go func() {
		defer wg.Done()

		for {
			select {
			case job, ok := <-jobs:
				if !ok {
					if len(batch) > 0 {
						fmt.Printf("process final batch: %v\n", batch)
					}
					return
				}

				batch = append(batch, job)

				if len(batch) == batchSize {
					fmt.Printf("process batch: %v\n", batch)
					batch = make([]int, 0, batchSize)
				}

			case <-time.After(500 * time.Millisecond):
				if len(batch) > 0 {
					fmt.Printf("process batch after timeout: %v\n", batch)
					batch = make([]int, 0, batchSize)
				}
			}
		}
	}()

	for i := 0; i < 5; i++ {
		jobs <- i
		time.Sleep(100 * time.Millisecond)
	}
	close(jobs)

	wg.Wait()
}
