package main

import "fmt"

// изначальная структура изменилась, так как мы сделали dereferencing

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
	fmt.Println(person.Name) // Bob
	ChangeName(person)
	fmt.Println(person.Name) // Alice
}
