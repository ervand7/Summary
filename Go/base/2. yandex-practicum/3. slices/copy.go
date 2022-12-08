package main

import "fmt"

func main() {
	src := []int{1, 2, 3, 4}

	var dest []int
	copy(dest, src)
	fmt.Println(dest) // []

	dest2 := make([]int, 3)
	copy(dest2, src)
	fmt.Println(dest2) // [1 2 3]

	dest3 := make([]int, 5)
	copy(dest3, src)
	fmt.Println(dest3) // [1 2 3 4 0]
}
