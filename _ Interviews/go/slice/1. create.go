package main

import "fmt"

func main() {
	var a []int
	fmt.Println(a, a == nil) // [] true

	var b = []int{}
	fmt.Println(b, b != nil) // [] true

	var c = make([]int, 0)
	fmt.Println(c, c != nil) // [] true

	var d = make([]int, 0)
	fmt.Println(d, d != nil) // [] true
}