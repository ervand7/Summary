package main

import (
	"sync"
)

// fatal error: concurrent map writes

func main() {
	var m = make(map[int]int)
	var wg sync.WaitGroup
	for i := 0; i < 10000; i++ {
		wg.Add(1)
		go func(item int) {
			defer wg.Done()
			m[item] = item
		}(i)
	}

	wg.Wait()
}
