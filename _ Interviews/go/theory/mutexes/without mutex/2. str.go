package main

import (
	"fmt"
	"sync"
)

func main() {
	var data string
	var wg sync.WaitGroup
	for i := 0; i < 10000; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			data += "1"
		}()
	}

	wg.Wait()

	fmt.Println(len(data)) // 2837
}
