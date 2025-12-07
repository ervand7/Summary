package main

import (
	"fmt"
	"sync"
)

type Stats struct {
	sum   int
	count int
}

func (s *Stats) Avg() float64 {
	if s.count == 0 {
		return 0
	}
	return float64(s.sum) / float64(s.count)
}

func (s *Stats) Add(v int) {
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
			fmt.Println(stats.Avg())
		}(i)
	}

	wg.Wait()
}
