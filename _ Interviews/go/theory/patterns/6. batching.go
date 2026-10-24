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
		batch     = make([]int, 0, batchSize)
		jobs      = make(chan int)
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

			case <-time.After(time.Millisecond * 500):
				if len(batch) > 0 {
					fmt.Printf("process batch: %v\n", batch)
					batch = make([]int, 0, batchSize)
				}
			}
		}
	}()

	for i := range 11 {
		jobs <- i
		time.Sleep(time.Millisecond * 100)
	}
	close(jobs)

	wg.Wait()
}
