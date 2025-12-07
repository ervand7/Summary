package main

import (
	"fmt"
	"sync"
)

type Counter struct {
	value int
}

func (c *Counter) Inc() {
	c.value++
}

func (c *Counter) Value() int {
	return c.value
}

func main() {
	c := &Counter{}
	var (
		wg sync.WaitGroup
		mu sync.Mutex
	)

	for i := 0; i < 10000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			defer mu.Unlock()
			mu.Lock()
			c.Inc()
		}()
	}

	wg.Wait()
	fmt.Println(c.Value())
}
