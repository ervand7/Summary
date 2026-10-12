package main

import "fmt"

func main() {
	roc := make(<-chan int)
	soc := make(chan<- int)

	fmt.Printf("%T\n", roc) // <-chan int
	fmt.Printf("%T\n", soc) // chan<- int
}
