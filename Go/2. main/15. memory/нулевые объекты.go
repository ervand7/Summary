package main

import (
	"fmt"
	"unsafe"
)

// В Go все нулевые структуры и массивы ссылаются на один и тот же адрес памяти

func main() {
	type s1 struct{}
	type s2 struct{}

	var a [0]int
	var b [0]int
	var c s1
	var d s2

	fmt.Println("a", unsafe.Pointer(&a)) // 0x102c0efc8
	fmt.Println("b", unsafe.Pointer(&b)) // 0x102c0efc8
	fmt.Println("c", unsafe.Pointer(&c)) // 0x102c0efc8
	fmt.Println("d", unsafe.Pointer(&d)) // 0x102c0efc8
}
