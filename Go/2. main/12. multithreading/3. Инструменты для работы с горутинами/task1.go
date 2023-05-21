package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup

	n := 10
	for i := 0; i < n-1; i++ {
		wg.Add(1)
		go func(v int) {
			fmt.Println(v)
			wg.Done()
		}(i)
	}
	wg.Wait()
}
