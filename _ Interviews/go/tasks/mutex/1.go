package main

import (
	"fmt"
	"sync"
)

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
