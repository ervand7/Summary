package main

import "fmt"

func SomeFunc() {
	a := "some text"
	// defer захватит значение <a> в то время, когда оно будет равно "some text"
	defer func(s string) { fmt.Println(s) }(a)
	a = "another text"
}
func main() {
	SomeFunc() // some text
}
