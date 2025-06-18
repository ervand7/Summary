package main

import "fmt"

func main() {
	ch := make(chan int)
	go func() {
		fmt.Println(<-ch)
	}()
	ch <- 1

}
