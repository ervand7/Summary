package main

import (
	"sync"
)

/*
We do not try to lock it more than 1 time. That's we no deadlock
*/

func main() {
	var x int
	mux := sync.Mutex{}

	mux.Lock()
	x += 1
}
