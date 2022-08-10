package main

import (
	"fmt"
	"unsafe"
)

func main() {
	var a struct{}
	// или
	b := struct{}{}

	fmt.Println(unsafe.Sizeof(a))   // 0
	fmt.Println(unsafe.Pointer(&b)) // 0x102ffefc8
}
