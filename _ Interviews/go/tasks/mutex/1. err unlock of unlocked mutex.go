package main

import (
	"fmt"
	"sync"
)

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
