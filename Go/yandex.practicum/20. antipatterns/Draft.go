package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

/* взрывоопасно */
func main() {

	a := "Hello, world"
	fmt.Println(a)

	stringHeader := (*reflect.StringHeader)(unsafe.Pointer(&a))
	*(*byte)(unsafe.Pointer(stringHeader.Data + 7)) = 'W'

	fmt.Println(a)
}
