package main

import "fmt"

func main() {
	type Vector[T any] []T

	// 1 variant
	var zero Vector[int]
	fmt.Println(zero) // []

	// 2 variant
	second := *new(Vector[int])
	fmt.Println(second) // []
}
