package main

import (
	"fmt"
	"unsafe"
)

func main() {
	type Foo struct {
		aaa int32 // 4
		bbb int32 // 4
		ccc int32 // 4
	}

	x := &Foo{}
	y := Foo{}

	fmt.Println(unsafe.Sizeof(x)) // 8
	fmt.Println(unsafe.Sizeof(y)) // 12
}
