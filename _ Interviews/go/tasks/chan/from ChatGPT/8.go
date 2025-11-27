package main

import "fmt"

// in this case it doesn't matter is the chan buffer or no. The buffer size also
// doesn't matter

func main() {
	ch := make(chan int, 1)

	go func() {
		ch <- 1
		ch <- 2
		ch <- 3
	}()

	fmt.Println(<-ch)
	fmt.Println(<-ch)
	fmt.Println(<-ch)
}
