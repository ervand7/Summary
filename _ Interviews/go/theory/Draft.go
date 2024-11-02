package main

import "fmt"

func main() {
	var a = []int{1, 2, 3}
	b := a
	fmt.Printf("%p\n", a)
	fmt.Printf("%p\n", b)
}
