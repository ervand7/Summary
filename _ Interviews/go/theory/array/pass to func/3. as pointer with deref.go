package main

import "fmt"

/*
Если передать его как pointer и применить dereferencing,
массив также изменится, так как работаем с одним и тем же адресом.
*/

func changeArrByPointer(arr *[4]int) {
	fmt.Printf("%p\n", arr) // 0x1400012c000
	(*arr)[1] = 121212
}

func main() {
	arr := [4]int{}
	fmt.Println(arr)         // [0 0 0 0]
	fmt.Printf("%p\n", &arr) // 0x1400012c000

	changeArrByPointer(&arr)
	fmt.Println(arr) // [0 121212 0 0]
}
