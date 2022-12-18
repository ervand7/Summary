package main

import (
	"fmt"
)

//пример без unsafe
func main() {
	array := [10]byte{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	slice := make([]byte, 5)
	copy(slice, array[:5])
	slice = append(slice, 42)
	fmt.Println(slice) // [0 1 2 3 4 42]
	fmt.Println(array) // [0 1 2 3 4 5 6 7 8 9]
}
