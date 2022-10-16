package main

import (
	"fmt"
	"unsafe"
)

func main() {
	// если напишем s := "123", то получим unexpected fault address
	s := fmt.Sprintf("%v%v%v", 1, 2, 3)
	fmt.Println(s)

	type stringStruct struct {
		str unsafe.Pointer
		len int
	}

	// do not do it in real code
	sInternal := (*stringStruct)(unsafe.Pointer(&s))
	fmt.Println(sInternal.len)

	// absolutely do not do it in real code
	((*[3]byte)(sInternal.str))[1] = '0'
	fmt.Println(s)
}
