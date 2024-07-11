package main

import (
	"fmt"
	"unsafe"
)

func main() {
	// anonymous struct
	a := struct{}{}
	fmt.Println(unsafe.Sizeof(a))  // 0
	fmt.Println(unsafe.Sizeof(&a)) // 8 - однако указатель будет весить не 0

	var b = struct {
		field1 int
		field2 int
		field3 int
		field4 int
		field5 int
	}{}
	// Видим, что просто объявленная и заполненная структуры весят одинаково
	fmt.Println(unsafe.Sizeof(b)) // 40
	b.field1 = 1
	b.field1 = 2
	b.field1 = 3
	b.field1 = 4
	b.field1 = 5
	fmt.Println(unsafe.Sizeof(b)) // 40
}
