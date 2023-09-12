package main

import (
	"fmt"
	"unsafe"
)

/*
All pointers have the same memory size and representation, which is 4 or 8
bytes that represent an address. On 32bit architectures (like the playground),
pointers require 4 bytes of memory and on 64 bit architectures (like your machine),
they require 8 bytes of memory.
*/

func main() {
	var a1 struct{}
	var a2 int
	var a3 string
	var a4 [4]int
	var a5 rune
	var a6 byte
	var a7 float32
	var a8 float64
	var a9 error
	var a10 any
	var a11 interface{}
	var a12 *any
	var a13 *func()
	var a14 chan any
	var a15 *map[int]int

	fmt.Println(unsafe.Sizeof(&a1))  // 8
	fmt.Println(unsafe.Sizeof(&a2))  // 8
	fmt.Println(unsafe.Sizeof(&a3))  // 8
	fmt.Println(unsafe.Sizeof(&a4))  // 8
	fmt.Println(unsafe.Sizeof(&a5))  // 8
	fmt.Println(unsafe.Sizeof(&a6))  // 8
	fmt.Println(unsafe.Sizeof(&a7))  // 8
	fmt.Println(unsafe.Sizeof(&a8))  // 8
	fmt.Println(unsafe.Sizeof(&a9))  // 8
	fmt.Println(unsafe.Sizeof(&a10)) // 8
	fmt.Println(unsafe.Sizeof(&a11)) // 8
	fmt.Println(unsafe.Sizeof(&a12)) // 8
	fmt.Println(unsafe.Sizeof(&a13)) // 8
	fmt.Println(unsafe.Sizeof(&a14)) // 8
	fmt.Println(unsafe.Sizeof(&a15)) // 8
}
