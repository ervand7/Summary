package main

import "fmt"

/*
Однако, если передать его как pointer, то массив изменится.
*/

func changeArrByDereferencing(arr *[4]int) {
	arr[1] = 121212
}

func main() {
	arr := [4]int{}
	fmt.Println(arr) // [0 0 0 0]

	changeArrByDereferencing(&arr)
	fmt.Println(arr) // [0 121212 0 0]
}
