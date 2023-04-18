package main

import "fmt"

/*
Мораль: когда берем слайс от слайса обрезая снизу - возвращается новый
адрес памяти
*/

func main() {
	a := []int{1, 2, 3}
	b := a
	c := b[:1]
	d := b[1:]
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130000
	fmt.Printf("%p\n", c) // 0x14000130000
	fmt.Printf("%p\n", d) // 0x14000130008
}
