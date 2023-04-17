package main

import "fmt"

/*
Однако, если передать его как pointer и применить dereferencing
массив изменится.
*/

func changeArrByDereferencing(arr *[4]int) {
	(*arr)[1] = 121212
}

func main() {
	arr := [4]int{}
	changeArrByDereferencing(&arr)
	fmt.Println(arr) // [0 121212 0 0]
}
