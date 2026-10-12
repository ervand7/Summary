package main

import (
	"sync"
)

func main() {
	var mu sync.Mutex
	mu.Lock() // 1
	go func() {
		mu.Unlock() // 3
	}()
	mu.Lock() // 2
}
