package main

import (
	"fmt"
	"unsafe"
)

func main() {
	type Foo struct {
		aaa bool  // 1 by default. But with padding - 4.
		bbb int32 // 4 as max in this struct.
	}

	x := &Foo{}
	y := Foo{}

	fmt.Println(unsafe.Sizeof(x)) // 8
	fmt.Println(unsafe.Sizeof(y)) // 8
}
