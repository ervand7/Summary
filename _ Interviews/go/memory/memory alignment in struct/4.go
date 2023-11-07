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

	type optimizedFoo struct {
		bbb int32 // 4 (max)
		// next three will take 4 together
		aaa bool
		ccc bool
		ddd bool
	}
	x2 := &optimizedFoo{}
	y2 := optimizedFoo{}
	fmt.Println(unsafe.Sizeof(x2)) // 8
	fmt.Println(unsafe.Sizeof(y2)) // 8
}
