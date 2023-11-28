package main

import "fmt"

/*
Но если мы имеем дело с непустыми слайсами, то append во втором слайсе
будет аффектить на первый
*/

func main() {
	a := make([]int, 10)
	b := a[:len(a)-1]
	fmt.Println(a)        // [0 0 0 0 0 0 0 0 0 0]
	fmt.Println(b)        // [0 0 0 0 0 0 0 0 0]
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130000

	b = append(b, 1)
	fmt.Println(a)        // [0 0 0 0 0 0 0 0 0 1]
	fmt.Println(b)        // [0 0 0 0 0 0 0 0 0 1]
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130000
}
