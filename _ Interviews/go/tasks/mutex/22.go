package main

import "sync"

func main() {
	var mu sync.RWMutex

	mu.RUnlock()
}
