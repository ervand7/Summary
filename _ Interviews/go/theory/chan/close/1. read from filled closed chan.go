package main

import "fmt"

func main() {
	ch := make(chan int, 5)
	ch <- 1
	ch <- 2
	ch <- 3
	ch <- 4
	ch <- 5

	for i := 0; i < 10; i++ {
		if i == 3 {
			close(ch)
		}
		fmt.Println(<-ch)
	}
}
