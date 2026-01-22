package main

import (
	"fmt"
	"sync"
	"time"
)

type S struct {
	mu sync.Mutex
	x  int
}

func main() {
	s := S{}

	go func(s S) {
		s.mu.Lock()
		s.x++
		s.mu.Unlock()
	}(s)

	s.mu.Lock()
	s.x++
	s.mu.Unlock()

	time.Sleep(time.Second)
	fmt.Println(s.x)
}
