package main

import (
	"fmt"
	"sync"
	"time"
)

// this explicitly shows the error from prev example

func main() {
	ch := make(chan int)

	go func() {
		for i := 1; i <= 4; i++ {
			ch <- i
		}
		close(ch)
	}()

	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		time.Sleep(time.Second)
		ch <- 999
	}()

	for n := range ch {
		fmt.Println(n)
	}

	wg.Wait()
}
