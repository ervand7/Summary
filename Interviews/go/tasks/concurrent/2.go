package main

import (
	"fmt"
	"sync"
)

func main() {
	var max int

	mux := sync.Mutex{}
	for i := 10000; i > 0; i-- {
		go func(item int) {
			mux.Lock()
			if item%2 == 0 && item > max {
				max = item
			}
			mux.Unlock()
		}(i)
	}

	fmt.Printf("Maximum is %d", max) // Maximum is 10000
}
