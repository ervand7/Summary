package main

import "fmt"

/*
Если передать его как pointer и применить dereferencing,
массив также изменится.
*/

func changeArrByPointer(arr *[4]int) {
	(*arr)[1] = 121212
}

func main() {
	arr := [4]int{}
	fmt.Println(arr) // [0 0 0 0]

	changeArrByPointer(&arr)
	fmt.Println(arr) // [0 121212 0 0]
}
