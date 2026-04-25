package main

import "fmt"

func main() {
	a := make([]int, 0, 3)
	a = append(a, 1, 2)

	b := append(a, 3)
	c := append(a, 4)

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
