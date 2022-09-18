package main

import (
	"fmt"
	"time"
)

func main() {
	a := make(chan int)
	b := make(chan int)

	go func() {
		a <- 1
	}()
	go func() {
		b <- 2
	}()
	time.Sleep(10 * time.Millisecond)
	select {
	case v := <-a:
		fmt.Print(v)
	case v := <-b:
		fmt.Print(v)
	}
}

// select равновероятно выполнит один из двух вариантов (1 или 2)
