package main

import "fmt"

func main() {
	arr := make([]int, 4, 4)
	arr2 := append(arr, 1)
	fmt.Printf("%p\n", arr)
	fmt.Printf("%p\n", arr2)

	arr[0] = 5
	arr2[0] = 9

	fmt.Println(arr)  // [5 0 0 0]
	fmt.Println(arr2) // [9 0 0 0 1]
}
