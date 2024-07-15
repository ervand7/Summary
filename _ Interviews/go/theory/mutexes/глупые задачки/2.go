package main

import (
	"fmt"
	"sync"
)

/*
Удивительно, но без WaitGroup и Sleep программа выведет не 0, а какое-то число
от 0 до 99
*/

func main() {
	var mu sync.Mutex
	m := make(map[int]int)

	for i := 0; i < 100; i++ {
		go func(v int) {
			mu.Lock()
			m[v] = v
			mu.Unlock()
		}(i)
	}
	fmt.Println(len(m))
}
