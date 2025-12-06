package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int)
	go func() {
		for {
			ch <- 1
			fmt.Println("Hello")
		}
	}()

	val := <-ch
	fmt.Println(val)
	time.Sleep(time.Second * 5)
	fmt.Println("Ok")
}
