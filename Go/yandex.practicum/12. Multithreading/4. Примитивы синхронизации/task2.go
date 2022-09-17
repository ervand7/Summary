package main

import (
	"fmt"
	"sync"
)

func main() {
	var (
		mu sync.Mutex
		wg sync.WaitGroup
	)
	m := make(map[int]int)

	for i := 0; i < 100; i++ {
		wg.Add(1)
		go func(v int) {
			defer wg.Done()
			mu.Lock()
			m[v] = v
			mu.Unlock()
		}(i)
	}
	wg.Wait()
	fmt.Println(len(m))
}
