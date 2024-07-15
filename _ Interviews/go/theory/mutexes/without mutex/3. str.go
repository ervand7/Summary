package main

import (
	"fmt"
	"sync"
)

func main() {
	var slice = make([]int, 0)
	var wg sync.WaitGroup
	for i := 0; i < 10000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			slice = append(slice, 1)
		}()
	}

	wg.Wait()

	fmt.Println(len(slice)) // 8959
}
