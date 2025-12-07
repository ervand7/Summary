package main

import (
	"fmt"
	"sync"
)

type Store struct {
	mu   sync.RWMutex
	data map[string]int
}

func NewStore() *Store {
	return &Store{data: make(map[string]int)}
}

func (s *Store) Get(k string) int {
	s.mu.RLock()
	defer s.mu.RUnlock()
	return s.data[k]
}

func (s *Store) Set(k string, v int) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.data[k] = v
}

func main() {
	store := NewStore()
	var wg sync.WaitGroup

	for i := 0; i < 3000; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			store.Set("x", i)
		}(i)
	}

	for i := 0; i < 3000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			fmt.Println(store.Get("x"))
		}()
	}

	wg.Wait()
}
