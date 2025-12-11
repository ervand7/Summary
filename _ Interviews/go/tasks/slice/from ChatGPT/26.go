package main

import "fmt"

func main() {
	x := []int{5, 6, 7, 8}
	y := x[:2]
	z := append(y, 100, 200, 300)
	fmt.Println(x)
	fmt.Println(y)
	fmt.Println(z)
}
