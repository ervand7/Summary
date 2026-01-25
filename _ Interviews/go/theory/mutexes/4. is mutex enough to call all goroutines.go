package main

import (
	"fmt"
	"sync"
)

func main() {
	s := make([]int, 0, 10000)

	var mu sync.Mutex
	for i := 0; i < 10000; i++ {
		go func(v int) {
			mu.Lock()
			defer mu.Unlock()
			s = append(s, v)
		}(i)
	}

	fmt.Println(len(s))
}
