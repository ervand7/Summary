package main

import "fmt"

// struct will be changed because we make dereferencing

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
