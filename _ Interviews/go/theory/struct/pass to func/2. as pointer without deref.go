package main

import "fmt"

type Person struct {
	Name string
}

func changeByPointer(person *Person) {
	person = &Person{
		Name: "Alice",
	}
}

func main() {
	person := &Person{
		Name: "Bob",
	}
	changeByPointer(person)
	fmt.Println(person.Name)
}
