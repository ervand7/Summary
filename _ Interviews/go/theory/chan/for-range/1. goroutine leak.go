package main

import (
	"fmt"
)

func main() {
	ch := make(chan int)
	go func() {
		for v := range ch {
			fmt.Println(v)
		}
	}()

	for i := 0; i < 10; i++ {
		ch <- i
	}
}
