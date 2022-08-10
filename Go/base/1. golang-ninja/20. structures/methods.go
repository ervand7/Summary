package main

import "fmt"

type Some struct {
	name   string
	age    int
	sex    string
	weight int
	height int
}

func NewSome(name, sex string, age, weight, height int) Some {
	return Some{
		name:   name,
		sex:    sex,
		age:    age,
		weight: weight,
		height: height,
	}
}

func main() {
	some1 := NewSome("Vasya", "male", 25, 75, 185)
	some2 := NewSome("Petya", "male", 24, 80, 175)

	printSomeInfo(some1) // Vasya 25 male 75 185
	printSomeInfo(some2) // Petya 24 male 80 175
}

func printSomeInfo(some Some) {
	fmt.Println(some.name, some.age, some.sex, some.weight, some.height)
}
