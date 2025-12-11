package main

import "fmt"

type some struct {
	field string
}

func main() {
	var a = some{field: "q"}
	b := a

	b.field = "qwe"
	fmt.Println(a.field)
}
