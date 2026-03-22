package main

import (
	"fmt"
	"sync"
)

// Go scheduler only guarantees execution when there is blocking/synchronization.
// Here is no blocking, hence the scheduler will not be forced to awake the anon
// goroutine

func main() {
	i := 0
	mu := sync.Mutex{}

	go func() {
		mu.Lock()
		i = 1
	}()

	mu.Unlock()
	fmt.Println(i)
}
