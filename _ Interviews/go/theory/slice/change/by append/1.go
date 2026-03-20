package main

import "fmt"

// because we work with empty slice

func main() {
	a := make([]int, 0, 10)
	b := a

	b = append(b, 1)
	fmt.Println(a)
	fmt.Println(b)
}
