package main

import (
	"sync"
)

/*
Если забыть сделать Unlock() в горутине main, то получим deadlock.
Однако, если бы не было цикла, то не получили бы deadlock.
*/

func main() {
	var x int
	mux := sync.Mutex{}

	for i := 0; i < 3; i++ {
		mux.Lock()
		x += 1
		// mux.Unlock() // забыли разлочить
	}
}
