package main

import "fmt"

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
	changeByValue(human)
	fmt.Println(human.Name)
}
