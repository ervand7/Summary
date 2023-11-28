package main

import "fmt"

/*
Несмотря на то, что у обоих слайсов адрес памяти одинаковый, слайс `a` не изменится.
Это происходит из-за того, мы работаем с пустыми слайсами.
*/

func main() {
	a := make([]int, 0, 10)
	b := a
	fmt.Println(a)        // []
	fmt.Println(b)        // []
	fmt.Printf("%p\n", a) // 0x100966fc8
	fmt.Printf("%p\n", b) // 0x100966fc8

	b = append(b, 1)
	fmt.Println(a)        // []
	fmt.Println(b)        // [1]
	fmt.Printf("%p\n", a) // 0x100966fc8
	fmt.Printf("%p\n", b) // 0x100966fc8
}
