package main

import "fmt"

// изменится

type Some struct {
	field string
}

func main() {
	var a = &Some{field: "q"}
	b := a

	fmt.Printf("%p\n", a) // 0x14000110210
	fmt.Printf("%p\n", b) // 0x14000110220

	b.field = "qwe"
	fmt.Println(a.field) // qwe
}
