package main

import "fmt"

type MyStruct struct {
	field1 int
	field2 []int
}

func main() {
	a := MyStruct{
		field1: 1,
		field2: []int{1, 2, 3},
	}

	b := a

	b.field1 = 2
	fmt.Println(a.field1)

	b.field2[0] = 3
	fmt.Println(a.field2)

	b.field2 = append(b.field2, 3)
	fmt.Println(b.field2)
	fmt.Println(a.field2)
}
