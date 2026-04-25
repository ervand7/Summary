package main

import (
	"fmt"
	"sync"
	"time"
)

var (
	mu    sync.Mutex
	cond  = sync.NewCond(&mu)
	ready = false
)

func main() {
	// waiter
	go func() {
		mu.Lock()
		for !ready {
			cond.Wait() // releases lock and sleeps
		}
		fmt.Println("Data is ready!")
		mu.Unlock()
	}()

	// worker
	time.Sleep(1 * time.Second)

	mu.Lock()
	ready = true
	cond.Signal() // wake one waiter
	mu.Unlock()

	time.Sleep(1 * time.Second)
}
