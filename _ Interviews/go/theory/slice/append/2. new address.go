package main

import "fmt"

/*
Каждый раз, когда выделяется новый базовый массив, то при append мы получаем
объект с новым адресом
*/

func main() {
	arr := make([]int, 0)
	fmt.Printf("cap=%d %p \n", cap(arr), arr) // cap=0 0x102226fc8
	arr = append(arr, 1)
	fmt.Printf("cap=%d %p \n", cap(arr), arr) // cap=1 0x1400012c020
	arr = append(arr, 2)
	fmt.Printf("cap=%d %p \n", cap(arr), arr) // cap=2 0x1400012c030
	arr = append(arr, 3)
	fmt.Printf("cap=%d %p \n", cap(arr), arr) // cap=4 0x14000132020
	arr = append(arr, 4)
	fmt.Printf("cap=%d %p \n", cap(arr), arr) // cap=4 0x14000132020
	arr = append(arr, 5)
	fmt.Printf("cap=%d %p \n", cap(arr), arr) // cap=8 0x1400012c040
	arr = append(arr, 6)
	fmt.Printf("cap=%d %p \n", cap(arr), arr) // cap=8 0x1400012c040
	arr = append(arr, 7)
	fmt.Printf("cap=%d %p \n", cap(arr), arr) // cap=8 0x1400012c040
}
