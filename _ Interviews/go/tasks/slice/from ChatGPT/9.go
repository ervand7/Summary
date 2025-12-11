package main

import "fmt"

func main() {
	x := make([]int, 3)
	y := append(x, 1)
	x[0] = 99

	fmt.Println(x)
	fmt.Println(y)
}
