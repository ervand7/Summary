package main

import "fmt"

// Слайс не изменится

func changeArr(arr []int) {
	arr = append(arr, 5, 6, 7)
	fmt.Printf("%p\n", arr) // 0x14000076000
	fmt.Println(arr)        // [0 1 2 3 4 5 6 7]
}

func main() {
	arr := make([]int, 0, 50)
	arr = append(arr, 0, 1, 2, 3, 4)
	fmt.Printf("%p\n", arr) // 0x14000076000

	changeArr(arr)
	fmt.Println(arr) // [0 1 2 3 4]
}
