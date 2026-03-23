package main

import (
	"fmt"
	"sync"
)

type Stats struct {
	sum   int
	count int
	mu    sync.RWMutex
}

func (s *Stats) Avg() float64 {
	s.mu.RLock()
	defer s.mu.RUnlock()
	if s.count == 0 {
		return 0
	}
	return float64(s.sum) / float64(s.count)
}

func (s *Stats) Add(v int) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.sum += v
	s.count++
}

func main() {
	stats := &Stats{}
	var wg sync.WaitGroup

	for i := 0; i <= 10000; i++ {
		wg.Add(1)
		go func(i int) {
			defer wg.Done()
			stats.Add(i)
			fmt.Printf("count: %d, sum: %d, average: %f\n",
				stats.count, stats.sum, stats.Avg())
		}(i)
	}

	wg.Wait()
}
