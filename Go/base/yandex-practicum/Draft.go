package main

import "fmt"

type A struct{}

func (a A) Foo() string {
	return "a"
}

type B struct {
	A
}

func (b B) Foo() string {
	return "b"
}

type C struct {
	A
}

func main() {
	b := B{}
	c := C{}

	fmt.Println(b.Foo(), c.Foo())
}
