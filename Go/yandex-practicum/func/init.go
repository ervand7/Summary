package main

import "fmt"

var name, surname string

func init() {
	name = "John"
}
func init() {
	if surname == "" {
		surname = "Doe"
	}
}
func main() {
	fmt.Println("Hello " + name + " " + surname) // Hello John Doe
}
