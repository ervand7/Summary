package main

import "fmt"

type Man struct {
	Name string
}

func ChangeName(person *Man) {
	*person = Man{
		Name: "Alice",
	}
}

func main() {
	person := &Man{
		Name: "Bob",
	}
	ChangeName(person)
	fmt.Println(person.Name)
}
