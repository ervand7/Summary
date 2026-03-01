package main

import "fmt"

// LIFO

func main() {
	defer fmt.Println("defer 1")
	defer fmt.Println("defer 2")
	defer fmt.Println("defer 3")
}

/*
defer 3
defer 2
defer 1
*/
