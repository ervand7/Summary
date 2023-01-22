package main

import (
	"fmt"
	"unsafe"
)

func main() {
	a := struct{}{}                // anonymous struct
	fmt.Println(unsafe.Sizeof(a))  // 0
	fmt.Println(unsafe.Sizeof(&a)) // 8 - однако указатель будет весить не 0

	var b = struct {
		field1 int
	}{}
	// Видим, что просто объявленная и заполненная структуры весят одинаково
	fmt.Println(unsafe.Sizeof(b)) // 8
	b.field1 = 9
	fmt.Println(unsafe.Sizeof(b)) // 8
}
