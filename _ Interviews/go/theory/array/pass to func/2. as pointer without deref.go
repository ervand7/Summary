package main

import "fmt"

/*
Однако, если передать его как pointer, то массив изменится. Так как мы
имеем дело с одним и тем же адресом памяти.
*/

func changeArrByDereferencing(arr *[4]int) {
	fmt.Printf("%p\n", arr) // 0x140000b4000
	arr[1] = 121212
}

func main() {
	arr := [4]int{}
	fmt.Println(arr)         // [0 0 0 0]
	fmt.Printf("%p\n", &arr) // 0x140000b4000

	changeArrByDereferencing(&arr)
	fmt.Println(arr) // [0 121212 0 0]
}
