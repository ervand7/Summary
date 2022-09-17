package main

import (
	"fmt"
	"sync"
	"time"
)

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
	time.Sleep(1 * time.Second)
	fmt.Println(len(m))
}
