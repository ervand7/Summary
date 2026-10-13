package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var x int
	mux := sync.Mutex{}
	for i := 0; i < 10; i++ {
		go func() {
			mux.Lock()
			x += 1
			// mux.Unlock() // забыли разлочить
		}()
	}

	time.Sleep(time.Second)
	fmt.Println(x)
}
