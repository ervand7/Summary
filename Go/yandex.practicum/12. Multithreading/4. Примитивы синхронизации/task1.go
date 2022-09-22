package main

import (
	"fmt"
	"sync"
)

func main() {
	m := make(map[int]int)

	var mu sync.Mutex
	var wg sync.WaitGroup
	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func(v int) {
			mu.Lock()
			m[v] = v
			mu.Unlock()
			wg.Done()
		}(i)
	}
	wg.Wait()
	fmt.Println(m, "\n", len(m))
}
