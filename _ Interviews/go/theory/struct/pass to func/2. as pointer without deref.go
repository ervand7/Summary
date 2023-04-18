package main

import "fmt"

// ничего не изменилось, иак как мы не сделали dereferencing

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
	fmt.Println(person.Name) // Bob
	changeByPointer(person)
	fmt.Println(person.Name) // Bob
}
