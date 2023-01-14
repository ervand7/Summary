package main

import "fmt"

/*
Каждый раз, когда выделяется новый базовый массив, то при append мы получаем
объект с новым адресом
*/

func main() {
	arr := make([]int, 0)
	fmt.Printf("%p\n", arr) // 0x100efefc8
	arr = append(arr, 1)
	fmt.Printf("%p\n", arr) // 0x1400012c008
	arr = append(arr, 2)
	fmt.Printf("%p\n", arr) // 0x1400012c020
	arr = append(arr, 5)
	fmt.Printf("%p\n", arr) // 0x14000132000
}
