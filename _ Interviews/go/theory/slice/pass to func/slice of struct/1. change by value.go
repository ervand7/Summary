package main

import (
	"fmt"
)

type some struct {
	field1 int
	field2 string
}

func changeByValue(s []some) {
	for i := range s {
		s[i].field2 = "rty"
	}
}

func main() {
	a := some{
		field1: 1,
		field2: "qwe",
	}
	v := []some{a}
	changeByValue(v)

	fmt.Println(v)
}
