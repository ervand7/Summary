package main

import (
	"sync"
)

func main() {
	var x int
	mux := sync.Mutex{}

	for i := 0; i < 3; i++ {
		mux.Lock()
		x += 1
		// mux.Unlock() // забыли разлочить
	}
}
