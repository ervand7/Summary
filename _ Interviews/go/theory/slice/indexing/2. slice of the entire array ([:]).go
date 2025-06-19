package main

import "fmt"

func main() {
	var a = []int{1, 2, 3, 4, 5}
	b := a[:0]
	fmt.Println(b) // []
	// fmt.Println(b[1]) // panic: runtime error: index out of range [1] with length 0
	fmt.Println(b[:cap(b)]) // [1 2 3 4 5]
}
