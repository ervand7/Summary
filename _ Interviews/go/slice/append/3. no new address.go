package main

import "fmt"

/*
Однако, если дополнительной аллокации не происходит, то адрес
остается тот же.
*/

func main() {
	arr := make([]int, 0, 10)
	fmt.Printf("%d %p \n", cap(arr), arr) // 10 0x14000130000
	arr = append(arr, 1)
	fmt.Printf("%d %p \n", cap(arr), arr) // 10 0x14000130000
	arr = append(arr, 2)
	fmt.Printf("%d %p \n", cap(arr), arr) // 10 0x14000130000
	arr = append(arr, 3)
	fmt.Printf("%d %p \n", cap(arr), arr) // 10 0x14000130000
	arr = append(arr, 4)
	fmt.Printf("%d %p \n", cap(arr), arr) // 10 0x14000130000
	arr = append(arr, 5)
	fmt.Printf("%d %p \n", cap(arr), arr) // 10 0x14000130000
	arr = append(arr, 6)
	fmt.Printf("%d %p \n", cap(arr), arr) // 10 0x14000130000
	arr = append(arr, 7)
	fmt.Printf("%d %p \n", cap(arr), arr) // 10 0x14000130000
}
