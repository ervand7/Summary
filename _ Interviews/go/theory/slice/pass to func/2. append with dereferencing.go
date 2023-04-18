package main

import "fmt"

/*
Слайс изменился, так как мы сделали dereferencing.
*/

func changeByDereference(arr *[]int) {
	*arr = append(*arr, 5, 6, 7)
	fmt.Printf("%p\n", arr) // 0x1400000c030
	fmt.Println(*arr)       // [0 1 2 3 4 5 6 7]
}

func main() {
	arr := make([]int, 0, 50)
	arr = append(arr, 0, 1, 2, 3, 4)
	fmt.Println(arr)         // [0 1 2 3 4]
	fmt.Printf("%p\n", &arr) // 0x1400000c030

	changeByDereference(&arr)
	fmt.Println(arr) // [0 1 2 3 4 5 6 7]
}
