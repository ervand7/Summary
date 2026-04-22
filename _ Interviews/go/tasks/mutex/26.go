package main

import (
	"sync"
	"time"
)

func main() {
	var mu sync.Mutex

	go func() {
		mu.Lock()
		mu.Unlock()
		mu.Unlock()
	}()

	time.Sleep(time.Second)
	mu.Lock()
}
