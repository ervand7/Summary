package main

import (
	"fmt"
	"sync"
	"time"
)

// Тут не хватает sync.WaitGroup

func main() {
	var mu sync.Mutex
	m := make(map[int]int)

	for i := 0; i < 100; i++ {
		go func() {
			mu.Lock()
			m[i] = i
			mu.Unlock()
		}()
	}
	time.Sleep(1 * time.Second)
	fmt.Println(len(m))
}
