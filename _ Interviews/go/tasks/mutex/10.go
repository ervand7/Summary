package main

import (
	"fmt"
	"sync"
	"time"
)

// should be passed as pointer, but passed as val. That's why no changes

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
