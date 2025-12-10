package main

import (
	"fmt"
)

type Some struct {
	field1 int
	field2 string
}

func changeByPointer(s []*Some) {
	fmt.Printf("%p\n", s[0])

	for i := range s {
		s[i].field2 = "rty"
	}
}

func main() {
	a := Some{
		field1: 1,
		field2: "qwe",
	}
	v := []*Some{&a}
	fmt.Printf("%p\n", v[0])
	changeByPointer(v)

	fmt.Println(v[0])
}
