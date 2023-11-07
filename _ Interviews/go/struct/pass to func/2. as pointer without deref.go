package main

import "fmt"

// ничего не изменилось, так как мы просто перезатерли значение

type Person struct {
	Name string
}

func changeByPointer(person *Person) {
	fmt.Printf("%p\n", person) // 0x14000110210
	person = &Person{
		Name: "Alice",
	}
	fmt.Printf("%p\n", person) // 0x14000110230
}

func main() {
	person := &Person{
		Name: "Bob",
	}
	fmt.Println(person.Name) // Bob
	changeByPointer(person)
	fmt.Println(person.Name) // Bob
}
