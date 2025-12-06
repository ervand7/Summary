package main

import (
	"fmt"
	"sync"
	"time"
)

/*
There is a deadlock, but Go doesn’t report it because main is not waiting.
One goroutine locks the mutex and never unlocks it. All other goroutines block on Lock().
But main just Sleeps and exits, so the program finishes before Go can detect a global deadlock.
Deadlock is detected only when all goroutines are blocked and main is blocked too.*/

func main() {
	var x int
	mux := sync.Mutex{}
	for i := 0; i < 10; i++ {
		go func() {
			mux.Lock()
			x += 1
			fmt.Println(x)
			// mux.Unlock() // забыли разлочить
		}()
	}

	time.Sleep(time.Second)
}
