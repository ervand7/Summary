package main

import "fmt"

// значение изменилось, так как мы работали непосредственно с тем же адресом памяти

type Some struct {
	Name string
}

func changeFieldByPointer(person *Some) {
	fmt.Printf("%p\n", person) // 0x14000010230
	person.Name = "Alice"
}

func main() {
	person := &Some{
		Name: "Bob",
	}
	fmt.Printf("%p\n", person) // 0x14000010230
	fmt.Println(person.Name)   // Bob
	changeFieldByPointer(person)
	fmt.Println(person.Name) // Alice
}
