package main

import "fmt"

// изменится. Одинаковые адреса

type Some struct {
	field string
}

func main() {
	var a = &Some{field: "q"}
	b := a

	fmt.Printf("%p\n", a) // 0x1400008e040
	fmt.Printf("%p\n", b) // 0x1400008e040

	b.field = "qwe"
	fmt.Println(a.field) // qwe
}
