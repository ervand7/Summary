package main

import "sync"

func main() {
	var mu sync.Mutex

	if true {
		mu.Lock()
	}

	mu.Unlock()
	mu.Unlock()
}
