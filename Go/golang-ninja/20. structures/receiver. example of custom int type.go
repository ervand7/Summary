package main

import "fmt"

// Age declare custom int type
type Age int

// receiver
func (a Age) isAdult() bool {
	return a >= 18
}

type People struct {
	name   string
	age    Age
	sex    string
	weight int
	height int
}

func NewPeople(name, sex string, age, weight, height int) People {
	return People{
		name:   name,
		sex:    sex,
		age:    Age(age),
		weight: weight,
		height: height,
	}
}

func main() {
	usr := NewPeople("Vasya", "male", 25, 75, 185)
	fmt.Println(usr.age.isAdult()) // true
}
