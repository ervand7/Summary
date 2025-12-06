package main

import (
	"sync"
)

/*
Goroutine starts blocking only after second sequential mu.Lock() call.
- First mu.Lock() → succeeds immediately
 - go func() → goroutine is runnable
 - Second mu.Lock() → this is where main blocks
 Only here the scheduler must run other goroutines.
*/

func main() {
	var mu sync.Mutex
	mu.Lock() // 1
	go func() {
		mu.Unlock() // 3
	}()
	mu.Lock() // 2
}
