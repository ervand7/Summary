package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var mu sync.Mutex

	for i := 0; i < 2; i++ {
		go func() {
			mu.Lock()
			fmt.Println("hello")
		}()
	}

	time.Sleep(time.Second)
	fmt.Println("world")
	mu.Lock()
}
