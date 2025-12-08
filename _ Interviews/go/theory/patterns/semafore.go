package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	semaphore := make(chan struct{}, 3) // максимум 3 одновременно

	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
		semaphore <- struct{}{}

		go func(n int) {
			defer wg.Done()
			defer func() { <-semaphore }()
			fmt.Println("Task", n)
			time.Sleep(time.Second)
		}(i)
	}
	wg.Wait()
}
