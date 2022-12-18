package main

import "fmt"

func main() {
	array := [10]byte{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	fmt.Println(array) // [0 1 2 3 4 5 6 7 8 9]
	slice := array[:5]
	slice = append(slice, 42)
	fmt.Println(array) // [0 1 2 3 4 42 6 7 8 9]
}
