package main

import (
	"fmt"
	"unsafe"
)

func main() {
	var a bool
	fmt.Println(unsafe.Sizeof(a)) // 1

	a = false
	fmt.Println(unsafe.Sizeof(a)) // 1
	
	a = true
	fmt.Println(unsafe.Sizeof(a)) // 1
}
