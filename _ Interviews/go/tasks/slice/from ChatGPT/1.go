package main

import "fmt"

func main() {
	s := make([]int, 0, 3)
	a := append(s, 1)
	b := append(s, 2)
	c := append(s, 3)
	fmt.Println(s)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
