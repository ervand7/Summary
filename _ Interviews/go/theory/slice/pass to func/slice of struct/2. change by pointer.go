package main

import (
	"fmt"
)

type Some struct {
	field1 int
	field2 string
}

func changeByPointer(s []*Some) {
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
	changeByPointer(v)

	fmt.Println(v[0])
}
