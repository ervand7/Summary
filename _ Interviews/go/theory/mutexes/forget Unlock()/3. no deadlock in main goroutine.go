package main

import (
	"sync"
)

func main() {
	var x int
	mux := sync.Mutex{}

	mux.Lock()
	x += 1
}
