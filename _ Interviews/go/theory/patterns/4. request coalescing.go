package main

import (
	"fmt"
	"sync"
	"time"
)

/*
Request coalescing (aka “singleflight” idea)
Goal: if many goroutines request the same data → do one real call, others wait and
reuse the result.
*/

var (
	once sync.Once
	wg   sync.WaitGroup
)

func fetch(id int) string {
	once.Do(func() {
		fmt.Printf("Only one can be here: %d\n", id)
		time.Sleep(time.Second) // simulate hard work
	})

	return "data"
}

func main() {
	for i := range 5 {
		wg.Add(1)

		go func(id int) {
			defer wg.Done()
			fmt.Println(fetch(id))
		}(i)
	}

	wg.Wait()
}
