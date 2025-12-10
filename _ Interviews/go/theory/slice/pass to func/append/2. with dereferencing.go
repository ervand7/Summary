package main

import "fmt"

func changeByDereference(arr *[]int) {
	*arr = append(*arr, 5, 6, 7)
}

func main() {
	arr := make([]int, 0, 50)
	arr = append(arr, 0, 1, 2, 3, 4)

	changeByDereference(&arr)
	fmt.Println(arr)
}
