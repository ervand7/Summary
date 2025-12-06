package main

import "sync"

func main() {
	var mu sync.Mutex

	for i := 0; i < 3; i++ {
		mu.Lock()
		defer mu.Unlock()
	}
}
