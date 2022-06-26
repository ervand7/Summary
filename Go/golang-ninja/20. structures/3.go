package main

import "fmt"

type Person struct {
	name   string
	age    int
	sex    string
	weight int
	height int
}

func main() {
	person := Person{"Vasya", 23, "Male", 75, 185}
	fmt.Println(person.height) // 185
}
