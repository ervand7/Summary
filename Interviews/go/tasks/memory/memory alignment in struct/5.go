package main

import (
	"fmt"
	"unsafe"
)

func main() {
	type Foo struct {
		aaa bool
		bbb int64
		ccc bool
		ddd bool
	}

	x := &Foo{}
	y := Foo{}

	fmt.Println(unsafe.Sizeof(x)) // 8
	fmt.Println(unsafe.Sizeof(y)) // 12
}
