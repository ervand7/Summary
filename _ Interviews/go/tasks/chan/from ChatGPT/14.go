package main

import (
	"fmt"
	"sync"
	"sync/atomic"
)

/*
Goal:
Multiple goroutines increment a shared counter 1000 times each.
Counter must be correct (1000 * workers).
You CANNOT use sync.Mutex.
Allowed:
 channels
 atomic operations
 worker pools
Question:
Implement a safe counter mechanism.
*/

func main() {
	const workers = 5

	var wg sync.WaitGroup
	wg.Add(workers)

	counter := newCounter()

	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()
			for j := 0; j < 1000; j++ {
				counter.Inc()
			}
		}()
	}

	wg.Wait()
	fmt.Println("final:", counter.Value()) // must be 5000
}

type Counter struct {
	value atomic.Int64
}

func newCounter() *Counter {
	return &Counter{
		value: atomic.Int64{},
	}
}

func (c *Counter) Inc() {
	c.value.Add(1)
}

func (c *Counter) Value() int {
	return int(c.value.Load())
}
