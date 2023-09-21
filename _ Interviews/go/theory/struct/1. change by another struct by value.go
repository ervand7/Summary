package main

import "fmt"

// не изменится

type some struct {
	field string
}

func main() {
	var a = some{field: "q"}
	b := a

	fmt.Printf("%p\n", &a) // 0x14000110210
	fmt.Printf("%p\n", &b) // 0x14000110220

	b.field = "qwe"
	fmt.Println(a.field) // q
}
