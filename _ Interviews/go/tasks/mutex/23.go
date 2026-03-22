package main

import (
	"sync"
	"time"
)

func main() {
	var mu sync.Mutex

	go func() {
		mu.Lock()
	}()

	mu.Lock()
	time.Sleep(time.Second)
}
