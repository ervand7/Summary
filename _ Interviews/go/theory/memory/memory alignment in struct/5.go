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
	fmt.Println(unsafe.Sizeof(y)) // 24

	type optimizedFoo struct {
		bbb int64
		aaa bool
		ccc bool
		ddd bool
	}
	x2 := &optimizedFoo{}
	y2 := optimizedFoo{}
	fmt.Println(unsafe.Sizeof(x2)) // 8
	fmt.Println(unsafe.Sizeof(y2)) // 16
}
