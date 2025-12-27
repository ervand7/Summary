package main

import (
	"fmt"
	"sync"
)

func longOp(i int) {
	fmt.Println(i * 2)
}

func main() {
	some := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	someChan := make(chan int)
	var wg sync.WaitGroup
	for i := 0; i < 2; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for x := range someChan {
				longOp(x)
			}
		}()
	}

	for _, s := range some {
		someChan <- s
	}

	wg.Wait()
	close(someChan)
}
