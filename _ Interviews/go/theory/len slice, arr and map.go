package main

import "fmt"

// Declared array with length 10 will have 10 zeros
// Declared slice with length 10 will have 10 zeros
// Declared map with length 10 will be empty

func main() {
	arr := [10]int{}
	fmt.Println(arr) // [0 0 0 0 0 0 0 0 0 0]

	slice := make([]int, 10)
	fmt.Println(slice) // [0 0 0 0 0 0 0 0 0 0]

	m := make(map[int]int, 10)
	fmt.Println(m) // map[]
}
