package main

import (
	"fmt"
)

func main() {
	ch := make(chan int)

	go func() {
		ch <- 1
		fmt.Println("Hello")
		close(ch)
	}()

	value, ok := <-ch
	if ok {
		fmt.Println("Received value:", value)
	} else {
		fmt.Println("Channel is closed")
	}

	// Attempt to receive again
	value, ok = <-ch
	if ok {
		fmt.Println("Received value:", value)
	} else {
		fmt.Println("Channel is closed")
	}
}
