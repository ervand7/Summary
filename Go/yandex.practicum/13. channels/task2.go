package main

import "fmt"

func main() {
	a := make(chan int)
	b := make(chan int)

	go func() {
		a <- 100
	}()
	go func() {
		v := <-a
		b <- v
	}()
	fmt.Println(<-b)
}

// 100
