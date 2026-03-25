package main

import "fmt"

// Without capacity → new array each time → independent slices

func main() {
	s := make([]int, 0)
	a := append(s, 1)
	b := append(s, 2)
	c := append(s, 3)
	fmt.Println(s)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
