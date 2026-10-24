package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var (
		wg        sync.WaitGroup
		batchSize = 3
		jobs      = make(chan int)
		batch     = make([]int, 0, batchSize)
	)

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

	for i := range 11 {
		jobs <- i
		time.Sleep(100 * time.Millisecond)
	}
	close(jobs)

	wg.Wait()
}
