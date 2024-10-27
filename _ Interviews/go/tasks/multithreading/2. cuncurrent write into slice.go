package main

import (
	"fmt"
	"sync"
)

func main() {
	items := []int{0, 0, 0}

	wg := sync.WaitGroup{}
	wg.Add(3)

	go func() {
		defer wg.Done()
		items[0] = 1
	}()
	go func() {
		defer wg.Done()
		items[1] = 2
	}()
	go func() {
		defer wg.Done()
		items[2] = 3
	}()

	wg.Wait()
	fmt.Println(items)
}

// [1, 2, 3]
