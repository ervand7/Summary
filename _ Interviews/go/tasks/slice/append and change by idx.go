package main

import "fmt"

/*
Append не заафектит slice в main, так как slice был передан в changeOne как
value. Однако изменение индекса заафектит
*/

func changeOne(slice []int) {
	slice = append(slice, 5)
	slice[1] = 0
	fmt.Println(slice) // [0 0 2 3 4 5]
}

func main() {
	slice := make([]int, 0)
	slice = append(slice, 0, 1, 2, 3, 4)

	changeOne(slice)
	fmt.Println(slice) // [0 0 2 3 4]
}
