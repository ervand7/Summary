package main

import (
	"fmt"
)

// we do not see deadlock because the program finishes while a
// goroutine is still blocked — and Go does NOT panic if main
// returns while other goroutines are stuck.

func main() {
	ch := make(chan int, 1)

	go func() {
		fmt.Println(<-ch)
		ch <- 20
	}()

	ch <- 10
	ch <- 30

	fmt.Println("done")
}
