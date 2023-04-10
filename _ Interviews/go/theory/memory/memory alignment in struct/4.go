package main

import (
	"fmt"
	"unsafe"
)

func main() {
	type Foo struct {
		aaa bool  // 1
		bbb int32 // 4 (max)
		ccc bool  // 1
		ddd bool  // 1
	}

	x := &Foo{}
	y := Foo{}

	fmt.Println(unsafe.Sizeof(x)) // 8
	fmt.Println(unsafe.Sizeof(y)) // 12
}
