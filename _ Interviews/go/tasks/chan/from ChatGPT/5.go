package main

import (
	"fmt"
)

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
