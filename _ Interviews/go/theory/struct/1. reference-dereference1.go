package main

import "fmt"

// struct will not be changed because we not make dereferencing

type Person struct {
	Name string
}

func changeName(person *Person) {
	person = &Person{
		Name: "Alice",
	}
}

func main() {
	person := &Person{
		Name: "Bob",
	}
	fmt.Println(person.Name) // Bob
	changeName(person)
	fmt.Println(person.Name) // Bob
}
