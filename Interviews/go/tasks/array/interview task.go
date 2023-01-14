package main

import "fmt"

/*
Append не заафектит arr в main, так как arr был передан в changeOne как
value. Однако изменение индекса заафектит
*/

func changeOne(arr []int) {
	arr = append(arr, 5)
	arr[1] = 0
	fmt.Println(arr) // [0 0 2 3 4 5]
}

func main() {
	arr := make([]int, 0)
	arr = append(arr, 0, 1, 2, 3, 4)

	changeOne(arr)
	fmt.Println(arr) // [0 0 2 3 4]
}
