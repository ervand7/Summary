package main

import (
	"fmt"
	"sync"
)

func main() {
	s := make([]int, 10000)

	var wg sync.WaitGroup
	for i := 0; i < 10000; i++ {
		wg.Add(1)
		go func(v int) {
			defer wg.Done()
			s[v] = v
		}(i)
	}

	wg.Wait()
	fmt.Println(len(s))
}
