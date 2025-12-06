package main

import "sync"

func main() {
	var mu sync.Mutex

	for i := 0; i < 2; i++ {
		go func() {
			mu.Lock()
		}()
	}

	mu.Lock()
}
