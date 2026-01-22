package main

import (
	"fmt"
	"sync"
	"time"
)

type Cache struct {
	mu   sync.RWMutex
	data map[string]int
	ttl  map[string]time.Time
}

func NewCache() *Cache {
	return &Cache{
		data: make(map[string]int),
		ttl:  make(map[string]time.Time),
	}
}

func (c *Cache) Get(key string) (int, bool) {
	now := time.Now()

	c.mu.RLock()
	v, ok := c.data[key]
	exp, hasTTL := c.ttl[key]
	expired := hasTTL && now.After(exp)
	c.mu.RUnlock()

	if !ok {
		return 0, false
	}
	if !expired {
		return v, true
	}

	c.mu.Lock()
	defer c.mu.Unlock()

	// Re-check under full Lock: someone might have refreshed the key
	// between RUnlock and Lock.
	v, ok = c.data[key]
	if !ok {
		return 0, false
	}
	exp, hasTTL = c.ttl[key]
	if hasTTL && now.After(exp) {
		delete(c.data, key)
		delete(c.ttl, key)
		return 0, false
	}

	return v, true
}

func (c *Cache) Set(key string, value int, ttl time.Duration) {
	c.mu.Lock()
	defer c.mu.Unlock()

	c.data[key] = value
	if ttl > 0 {
		c.ttl[key] = time.Now().Add(ttl)
	} else {
		delete(c.ttl, key)
	}
}

func main() {
	cache := NewCache()
	var wg sync.WaitGroup

	cache.Set("a", 1, time.Second)

	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			if v, ok := cache.Get("a"); ok {
				fmt.Println("value:", v)
			} else {
				fmt.Println("expired")
			}
		}()
	}

	for i := 0; i < 3; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			cache.Set("a", i, 2*time.Second)
		}(i)
	}

	wg.Wait()
}
