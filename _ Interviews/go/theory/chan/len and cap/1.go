package main

import "fmt"

func main() {
	// buff
	a := make(chan int, 3)
	a <- 1
	a <- 2
	fmt.Printf("Length is %v and capacity is %v\n", len(a), cap(a))

	// not buff
	b := make(chan int)
	fmt.Printf("Length is %v and capacity is %v\n", len(b), cap(b))
}

/*
Length is 2 and capacity is 3
Length is 0 and capacity is 0
*/
