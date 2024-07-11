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

	ticker := time.NewTicker(time.Second)

	for {
		select {
		case <-ticker.C:
			return
		case v := <-a:
			fmt.Println(v)
		case v := <-b:
			fmt.Println(v)
		}
	}
}
