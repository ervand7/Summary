package main

import (
	"fmt"
	"sync"
)

// Тут не хватает sync.WaitGroup

func main() {
	var mu sync.Mutex
	m := make(map[int]int)

	for i := 0; i < 100; i++ {
		go func(v int) {
			mu.Lock()
			m[v] = v
			mu.Unlock()
		}(i)
	}
	fmt.Println(len(m))
}
