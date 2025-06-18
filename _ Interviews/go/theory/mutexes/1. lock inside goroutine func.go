package main

import (
	"fmt"
	"sync"
)

func main() {
	var maximum int
	wg := sync.WaitGroup{}
	mux := sync.Mutex{}

	for i := 10000; i > 0; i-- {
		wg.Add(1)
		go func(item int) {
			mux.Lock()
			if item%2 == 0 && item > maximum {
				maximum = item
			}
			mux.Unlock()
			wg.Done()
		}(i)
	}

	wg.Wait()
	fmt.Printf("Maximum is %d", maximum) // Maximum is 10000
}
