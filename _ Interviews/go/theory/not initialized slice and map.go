package main

import "fmt"

// Not initialized array is NOT nil
// Not initialized slice is nil
// Not initialized map is nil

func main() {
	var arr [0]int
	fmt.Println(arr) // []

	var slice []int
	fmt.Println(slice) // nil

	var hTable map[int]int
	fmt.Println(hTable) // nil
}
