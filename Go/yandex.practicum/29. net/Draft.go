package main

import "fmt"

var first = 1
var second = 2

func ervand() {
	first = 4
	second = 9
	fmt.Println(first, second)
}

func main() {
	fmt.Println(first, second)

	ervand()
	fmt.Println(first, second)
}
