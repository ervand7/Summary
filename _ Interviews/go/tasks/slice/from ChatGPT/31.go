package main

import "fmt"

func foo1(a []int) []int {
	a = append(a, 7)
	return a
}

func main() {
	x := make([]int, 0, 1)
	x = append(x, 1)
	y := foo1(x)
	y[0] = 100
	fmt.Println(x)
	fmt.Println(y)
}
