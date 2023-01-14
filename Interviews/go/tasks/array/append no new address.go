package main

import "fmt"

/*
Каждый раз, когда выделяется новый базовый массив, то при append мы получаем
объект с новым адресом.

Однако, если дополнительной аллокации не происходит, то адрес остается тот же.
*/

func main() {
	arr := make([]int, 0, 100)
	fmt.Printf("%p\n", arr) // 0x14000130000
	arr = append(arr, 1)
	fmt.Printf("%p\n", arr) // 0x14000130000
	arr = append(arr, 2)
	fmt.Printf("%p\n", arr) // 0x14000130000
	arr = append(arr, 5)
	fmt.Printf("%p\n", arr) // 0x14000130000
}
