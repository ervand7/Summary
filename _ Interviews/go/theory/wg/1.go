package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup

	n := 10
	wg.Add(n)
	for i := 0; i < n-1; i++ {
		go func(v int) {
			fmt.Println(v)
			wg.Done()
		}(i)
	}

	wg.Wait()
}
