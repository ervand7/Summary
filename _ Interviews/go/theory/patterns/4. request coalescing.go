package main

import (
	"fmt"
	"sync"
	"time"
)

/*
Request coalescing (aka “singleflight” idea)
Goal: if many goroutines request the same data → do one real call, others wait and
reuse the result.
*/

var (
	mu      sync.Mutex
	loading bool
	result  string
	waitCh  = make(chan struct{})
)

func fetch() string {
	mu.Lock()

	if loading {
		mu.Unlock()
		<-waitCh // wait for result
		return result
	}

	loading = true
	mu.Unlock()
	fmt.Println("only one will be here")

	time.Sleep(1 * time.Second) // simulate hard work
	result = "data"

	mu.Lock()
	loading = false
	close(waitCh) // wake all waiters
	mu.Unlock()

	return result
}

func main() {
	for i := 0; i < 5; i++ {
		go func(id int) {
			fmt.Println(id, fetch())
		}(i)
	}

	time.Sleep(2 * time.Second)
}
