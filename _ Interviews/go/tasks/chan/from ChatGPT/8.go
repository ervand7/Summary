package main

import "fmt"

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
