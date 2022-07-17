package main

import "fmt"

func SomeFunc() {
	a := "some text"
	defer func(s string) { fmt.Println(s) }(a)
	a = "another text"
}
func main() {
	SomeFunc() // some text
}
