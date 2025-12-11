package main

import "fmt"

type Some struct {
	Name string
}

func changeFieldByPointer(person *Some) {
	person.Name = "Alice"
}

func main() {
	person := &Some{
		Name: "Bob",
	}
	changeFieldByPointer(person)
	fmt.Println(person.Name)
}
