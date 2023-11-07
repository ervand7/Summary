package main

import "fmt"

/*
Также при непустых слайсах, первый слайс поменяется даже если будут
разные адреса
*/

func main() {
	a := make([]int, 10)
	b := a[1 : len(a)-1]
	fmt.Println(a)        // [0 0 0 0 0 0 0 0 0 0]
	fmt.Println(b)        // [0 0 0 0 0 0 0 0]
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130008

	b = append(b, 1)
	fmt.Println(a)        // [0 0 0 0 0 0 0 0 0 1]
	fmt.Println(b)        // [0 0 0 0 0 0 0 0 1]
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130008
}
