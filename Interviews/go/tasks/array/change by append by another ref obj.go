package main

import "fmt"

// слайс a не изменится

func main() {
	a := make([]int, 0, 10)
	b := a
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130000

	b = append(b, 1)
	fmt.Println(a)        // []
	fmt.Println(b)        // [1]
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130000
}
