package main

import (
	"sync"
	"testing"
)

type CacheRW struct {
	mu   sync.RWMutex
	data map[string]int
}

type CacheM struct {
	mu   sync.Mutex
	data map[string]int
}

func NewCacheRW() *CacheRW {
	return &CacheRW{data: make(map[string]int)}
}

func NewCacheM() *CacheM {
	return &CacheM{data: make(map[string]int)}
}

// ————— RWMutex —————

func (c *CacheRW) Get(key string) int {
	c.mu.RLock()
	defer c.mu.RUnlock()
	return c.data[key]
}

func (c *CacheRW) Set(key string, v int) {
	c.mu.Lock()
	c.data[key] = v
	c.mu.Unlock()
}

// ————— Mutex —————

func (c *CacheM) Get(key string) int {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.data[key]
}

func (c *CacheM) Set(key string, v int) {
	c.mu.Lock()
	c.data[key] = v
	c.mu.Unlock()
}

// ————— Benchmarks —————

// 99% reads, 1% writes
func BenchmarkRWMutex_ReadHeavy(b *testing.B) {
	cache := NewCacheRW()
	cache.Set("x", 1)

	b.RunParallel(func(pb *testing.PB) {
		i := 0
		for pb.Next() {
			if i%100 == 0 {
				cache.Set("x", i)
			} else {
				cache.Get("x")
			}
			i++
		}
	})
}

func BenchmarkMutex_ReadHeavy(b *testing.B) {
	cache := NewCacheM()
	cache.Set("x", 1)

	b.RunParallel(func(pb *testing.PB) {
		i := 0
		for pb.Next() {
			if i%100 == 0 {
				cache.Set("x", i)
			} else {
				cache.Get("x")
			}
			i++
		}
	})
}
