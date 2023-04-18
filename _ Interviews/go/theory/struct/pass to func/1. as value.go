package main

import "fmt"

// ничего не изменится, так как мы передали значение структуры

type Human struct {
	Name string
}

func changeByValue(human Human) {
	human = Human{
		Name: "Alice",
	}
}

func main() {
	human := Human{
		Name: "Bob",
	}
	fmt.Println(human.Name) // Bob
	changeByValue(human)
	fmt.Println(human.Name) // Bob
}
