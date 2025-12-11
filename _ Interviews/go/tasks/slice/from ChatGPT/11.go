package main

import "fmt"

func foo(a, b []int) {
	copy(a, b)
	a = append(a, 7)
	b = append(b, 8)
}

func main() {
	x := []int{1, 1, 1, 1}
	y := []int{2, 2}
	foo(x, y)
	fmt.Println(x)
	fmt.Println(y)
}
