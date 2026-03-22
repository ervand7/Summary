package main

import (
	"sync"
	"time"
)

// Main does not wait forever, it just sleeps and exits.
// Deadlock requires all goroutines to be permanently blocked with no progress
// possible while program is still running

func main() {
	var mu sync.Mutex

	go func() {
		mu.Lock()
		mu.Unlock() // <-- never executed
		mu.Unlock() // <-- never executed
	}()

	mu.Lock()
	time.Sleep(time.Second)
}
