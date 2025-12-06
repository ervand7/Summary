package main

import (
	"sync"
	"time"
)

// 1) main locks the mutex and never blocks (it just sleeps).
// 2) The goroutine blocks on mu.Lock(), waiting.
// 3) After time.Sleep, main returns → program terminates.
// 4) Go runtime does not report deadlock if the program can still finish.

func main() {
	var mu sync.Mutex

	go func() {
		mu.Lock()
		mu.Unlock()
		mu.Unlock()
	}()

	mu.Lock()
	time.Sleep(time.Second)
}
