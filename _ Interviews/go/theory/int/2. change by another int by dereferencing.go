package main

import "fmt"

/*
Но с dereferencing все поменяется.
*/

func main() {
	a := 1
	b := &a

	fmt.Printf("%p\n", &a) // 0x1400000e0a0
	fmt.Printf("%p\n", b)  // 0x1400000e0a0

	*b = 777
	fmt.Printf("%p\n", b) // 0x1400000e0a0

	fmt.Println(a)  // 777
	fmt.Println(*b) // 777
}
