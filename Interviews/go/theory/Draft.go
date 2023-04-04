package main

import "fmt"

func main() {
	var a = make([]int, 0, 0)
	b := a
	fmt.Printf("%p\n", a)
	fmt.Printf("%p\n", b)
}
