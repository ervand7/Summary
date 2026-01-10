package main

import (
	"fmt"
	"sync"
)

func longOp(i int) {
	fmt.Println(i * 2)
}

func main() {
	arr := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	ch := make(chan int)
	var wg sync.WaitGroup
	for i := 0; i < 2; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for x := range ch {
				longOp(x)
			}
		}()
	}

	for _, s := range arr {
		ch <- s
	}

	wg.Wait()
	close(ch)
}
