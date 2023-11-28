package main

import "fmt"

/*
Слайс изменился, так как мы передали ссылку и сделали dereferencing.
*/

func changeByDereference(arr *[]int) {
	*arr = append(*arr, 5, 6, 7)
	fmt.Printf("%p\n", *arr) // 0x14000126000
	fmt.Println(*arr)        // [0 1 2 3 4 5 6 7]
}

func main() {
	arr := make([]int, 0, 50)
	arr = append(arr, 0, 1, 2, 3, 4)
	fmt.Println(arr)        // [0 1 2 3 4]
	fmt.Printf("%p\n", arr) // 0x14000126000

	changeByDereference(&arr)
	fmt.Println(arr) // [0 1 2 3 4 5 6 7]
}
