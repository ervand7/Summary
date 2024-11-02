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

	mu.Unlock()
	fmt.Println(i)
}
