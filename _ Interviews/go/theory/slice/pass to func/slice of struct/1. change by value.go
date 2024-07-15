package main

import (
	"fmt"
)

// поле у структуры изменится

type some struct {
	field1 int
	field2 string
}

func changeByValue(s []some) {
	fmt.Printf("%p\n", &s[0]) // 0x1400011e018

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
	fmt.Printf("%p\n", &v[0]) //  0x1400011e018
	changeByValue(v)

	fmt.Println(v) // [{1 rty}]
}
