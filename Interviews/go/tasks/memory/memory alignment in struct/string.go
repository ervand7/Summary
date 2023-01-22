package main

import (
	"fmt"
	"unsafe"
)

// unsafe.Sizeof для любой строки будет выдавать 16 байт
// https://stackoverflow.com/questions/65878177/unsafe-sizeof-says-any-string-takes-16-bytes-but-how

func main() {
	var a string
	fmt.Println(unsafe.Sizeof(a)) // 16

	a = "Hello world"
	fmt.Println(unsafe.Sizeof(a)) // 16
}
