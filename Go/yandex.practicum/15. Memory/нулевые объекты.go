package main

import (
	"fmt"
	"unsafe"
)

func main() {
	type s1 struct{}
	type s2 struct{}

	var a [0]int
	var b s1
	var c s2

	var s []int // у слайса адрес памяти будет другим

	fmt.Println("a", unsafe.Pointer(&a)) // 0x102c0efc8
	fmt.Println("a", unsafe.Pointer(&b)) // 0x102c0efc8
	fmt.Println("a", unsafe.Pointer(&c)) // 0x102c0efc8
	fmt.Println("a", unsafe.Pointer(&s)) // 0x1400011e018

}
