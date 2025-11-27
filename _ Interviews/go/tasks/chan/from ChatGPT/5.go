package main

import (
	"fmt"
)

// this chan closing is dangerous, because there are more than one writer

func main() {
	ch := make(chan int)

	go func() {
		for i := 1; i <= 4; i++ {
			ch <- i
		}
		close(ch)
	}()

	go func() {
		ch <- 999
	}()

	for n := range ch {
		fmt.Println(n)
	}
}
