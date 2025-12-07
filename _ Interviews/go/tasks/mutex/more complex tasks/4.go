package main

import (
	"fmt"
	"sync"
	"time"
)

type Cache struct {
	mu   sync.Mutex
	data map[int]int
}

func (c *Cache) Get(k int) (int, bool) {
	c.mu.Lock()
	defer c.mu.Unlock()
	v, ok := c.data[k]
	return v, ok
}

func (c *Cache) Set(k, v int) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.data[k] = v
}

func main() {
	cache := &Cache{data: make(map[int]int)}
	var wg sync.WaitGroup

	for i := 0; i < 10000; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			cache.Set(i, i*i)
		}(i)
	}

	time.Sleep(10 * time.Millisecond)

	for i := 0; i < 10000; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			if v, ok := cache.Get(i); ok {
				fmt.Println(v)
			}
		}(i)
	}

	wg.Wait()
}
