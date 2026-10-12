package main

import (
	"fmt"
	"sync"
)

func main() {
	ch := make(chan int, 10)

	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		for v := range ch {
			fmt.Println(v)
		}
	}()

	for i := 0; i < 5; i++ {
		ch <- i
	}

	wg.Wait()
}
