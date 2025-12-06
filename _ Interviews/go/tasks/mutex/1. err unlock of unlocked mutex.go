package main

import (
	"fmt"
	"sync"
)

// Go allows lock mutex in ane goroutine and unlock it in another. But it is
// bad and error-prone pattern.

// fatal error: sync: unlock of unlocked mutex

func main() {
	i := 0
	mu := sync.Mutex{}

	go func() {
		mu.Lock()
		i = 1
	}()

	// time.Sleep(time.Second) // но со слипом проблем не будет, так как горутина успеет запуститься
	mu.Unlock()
	fmt.Println(i)
}
