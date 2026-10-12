package main

import (
	"fmt"
)

func main() {
	ch := make(chan int, 10)
	go func() {
		for v := range ch {
			fmt.Println(v)
		}
	}()

	for i := 0; i < 5; i++ {
		ch <- i
	}
}
