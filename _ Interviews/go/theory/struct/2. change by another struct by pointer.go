package main

import "fmt"

type Some struct {
	field string
}

func main() {
	var a = &Some{field: "q"}
	b := a

	b.field = "qwe"
	fmt.Println(a.field)
}
