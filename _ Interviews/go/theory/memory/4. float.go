package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

func main() {
	var a = 1.0                    // will default to 8 byte
	fmt.Println(reflect.TypeOf(a)) // float64
	fmt.Println(unsafe.Sizeof(a))  // 8

	var b float32 = 1.0
	fmt.Println(unsafe.Sizeof(b))  // 4
	fmt.Println(reflect.TypeOf(b)) // float32

	// также можно задать целочисленное значение
	var c float64 = 1
	fmt.Println(unsafe.Sizeof(c))  // 8
	fmt.Println(reflect.TypeOf(c)) // float64
}
