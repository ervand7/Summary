package main

import "fmt"

/*
Когда берем слайс от слайса обрезая снизу - возвращается новый
адрес памяти
*/

func main() {
	a := []int{1, 2, 3}
	fmt.Printf("%p\n", a) // 0x14000130000

	b := a
	fmt.Printf("%p\n", b) // 0x14000130000

	c := b[:1]
	fmt.Printf("%p\n", c) // 0x14000130000

	d := b[1:]
	fmt.Printf("%p\n", d) // 0x14000130008
}
