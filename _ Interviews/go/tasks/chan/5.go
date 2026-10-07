package main

import "fmt"

func squares(ch chan int) {
	for i := 0; i <= 3; i++ {
		num := <-ch
		fmt.Println(num * num)
	}
}

func main() {
	fmt.Println("main() started")
	ch := make(chan int, 3)

	go squares(ch)

	ch <- 1
	ch <- 2
	ch <- 3
	ch <- 4 // blocks here

	fmt.Println("main() stopped")
}
