package main

import (
	"fmt"
	"unsafe"
)

func main() {
	type Foo struct {
		aaa bool  // 1 by default. But with padding - 4.
		bbb int32 // 4 as max in this struct.
		ccc bool  // 1 by default. But with padding - 4.
	}
	x := &Foo{}
	y := Foo{}
	fmt.Println(unsafe.Sizeof(x)) // 8
	fmt.Println(unsafe.Sizeof(y)) // 12

	type optimizeFoo struct {
		bbb int32 // 4 as max in this struct.
		// next two will take 4 together
		aaa bool
		ccc bool
	}
	x2 := &optimizeFoo{}
	y2 := optimizeFoo{}
	fmt.Println(unsafe.Sizeof(x2)) // 8
	fmt.Println(unsafe.Sizeof(y2)) // 8

}
