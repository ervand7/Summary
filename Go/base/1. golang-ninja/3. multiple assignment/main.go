package main

import "fmt"

func main() {
	a, b, c := 1, 2, 3
	fmt.Println(a, b, c) // 1, 2, 3

	a, b = b, a
	fmt.Println(a, b) // 2, 1
}
