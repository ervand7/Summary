package main

import (
	"fmt"
	"time"
)

// there is no deadlock because the main goroutine is not blocked (it sleeps
// and then exits), so not all goroutines are blocked at the same time.

func main() {
	ch := make(chan int)

	go func() {
		for i := 1; i <= 3; i++ {
			ch <- i
		}
		ch <- 999
	}()

	for i := 0; i < 3; i++ {
		fmt.Println(<-ch)
	}

	time.Sleep(time.Second)
}
