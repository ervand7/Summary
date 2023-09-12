package main

import "fmt"

// Скопируется столько элементов, сколько может вместить dst

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := make([]int, 5)
	var c []int
	d := make([]int, 10)

	copy(b, a)
	copy(c, a)
	copy(d, a)

	fmt.Println(a) // [1 2 3 4 5]
	fmt.Println(b) // [1 2 3 4 5]
	fmt.Println(c) // []
	fmt.Println(d) // [1 2 3 4 5 0 0 0 0 0]
}
