package main

import (
	"sync"
	"time"
)

func main() {
	var mu sync.Mutex

	go func(m *sync.Mutex) {
		m.Lock()
	}(&mu)

	time.Sleep(time.Second)
	mu.Lock()
}
