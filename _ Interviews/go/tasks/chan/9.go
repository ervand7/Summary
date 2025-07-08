package main

import (
	"fmt"
	"sync"
	"time"
)

// Implement semaphore with many writers and single reader

func main() {
	var (
		semaphore = make(chan int, 10)
		ch        = make(chan int)
	)

	// reader
	go func() {
		for val := range ch {
			fmt.Printf("processing value %d\n", val)
		}
	}()

	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		semaphore <- i
		ch <- i

		wg.Add(1)
		go func(wg *sync.WaitGroup) {
			wg.Done()
			time.Sleep(time.Second)
			<-semaphore
		}(&wg)

	}

	wg.Wait()
	close(ch)
}
