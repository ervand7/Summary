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
	once   sync.Once
	result string
)

func fetch() string {
	once.Do(func() {
		fmt.Println("only one will be here")
		time.Sleep(time.Second)
		result = "data"
	})

	return result
}

func main() {
	var wg sync.WaitGroup

	for i := range 5 {
		wg.Add(1)

		go func(id int) {
			defer wg.Done()
			fmt.Println(id, fetch())
		}(i)
	}

	wg.Wait()
}
