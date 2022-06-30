package main

import "fmt"

func main() {
	type Name string
	type Fruit string

	var fruit Fruit
	var name Name

	fruit = "Apple"
	name = Name(fruit) // так, после приведения типов, работает
	fmt.Println(name)
}
