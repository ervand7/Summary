package main

import "sync"

// No deadlock because RWMutex allows multiple readers simultaneously; RLock()
// is shared, not exclusive.

func main() {
	var mu sync.RWMutex

	mu.RLock()
	mu.RLock()
	mu.RLock()
}
