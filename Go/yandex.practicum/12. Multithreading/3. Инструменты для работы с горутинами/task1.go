package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup

	n := 10
	wg.Add(n - 1) // при wg.Add(n) будет fatal error: all goroutines are asleep - deadlock!
	for i := 0; i < n-1; i++ {
		go func(v int) {
			fmt.Println(v)
			wg.Done()
		}(i)
	}
	wg.Wait()
}
