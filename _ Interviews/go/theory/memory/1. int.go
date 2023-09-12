package main

import (
	"fmt"
	"unsafe"
)

func main() {
	var a = 1                     // will default to 8 byte (int/int64)
	fmt.Println(unsafe.Sizeof(a)) // 8

	var a1 int = 1
	fmt.Println(unsafe.Sizeof(a1)) // 8

	var b int8 = 1
	fmt.Println(unsafe.Sizeof(b)) // 1

	var c int16 = 1
	fmt.Println(unsafe.Sizeof(c)) // 2

	var d int32 = 1
	fmt.Println(unsafe.Sizeof(d)) // 4

	var e int64 = 1
	fmt.Println(unsafe.Sizeof(e)) // 8
}
