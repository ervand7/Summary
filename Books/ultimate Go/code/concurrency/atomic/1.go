package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

/*
Atomics provide synchronization at the hardware level.
*/

var counter int32

func main() {
	const grs = 2
	var wg sync.WaitGroup
	wg.Add(grs)
	for g := 0; g < grs; g++ {
		go func() {
			for i := 0; i < 2; i++ {
				atomic.AddInt32(&counter, 1)
			}
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println("Counter:", counter)
}
