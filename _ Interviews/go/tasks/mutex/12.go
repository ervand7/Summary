package main

import "sync"

func main() {
	var mu sync.RWMutex

	mu.Lock()
	mu.RUnlock()
}
