package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int, 1)

	go func() {
		fmt.Println(<-ch)
		ch <- 20
	}()

	ch <- 10
	ch <- 30

	time.Sleep(time.Second)
	fmt.Println("done")
}
