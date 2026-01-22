package main

import (
	"sync"
)

func main() {
	var mu sync.Mutex
	go func() { mu.Unlock() }()
	mu.Lock()
	mu.Lock()
}
