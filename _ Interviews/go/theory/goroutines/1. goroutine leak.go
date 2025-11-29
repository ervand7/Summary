package main

import (
	"fmt"
)

/*
Here is normal input but goroutine leak in anonymous goroutine.
*/

func main() {
	ch := make(chan int)
	go func() {
		for v := range ch {
			fmt.Println(v)
		}
	}()

	for i := 0; i < 10; i++ {
		ch <- i
	}

	// close(ch) // <- required to stop anonymous goroutine
}
