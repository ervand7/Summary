package main

import (
	"sync"
)

func main() {
	var mu sync.Mutex
	mu.Lock()
	mu.Lock()
}
