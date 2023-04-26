package main

import "fmt"

func main() {
	type A struct {
		IntField int
	}

	p := &A{}
	(*p).IntField = 42 // вместо (*p).IntField = 42

	fmt.Printf("%#v", p)
}
