package main

import (
	"fmt"
	"time"
)

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
