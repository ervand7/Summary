package main

import "fmt"

func main() {
	arr := make([]int, 4)
	arr2 := append(arr, 1)

	arr[0] = 5
	arr2[0] = 9

	fmt.Println(arr)
	fmt.Println(arr2)
}
