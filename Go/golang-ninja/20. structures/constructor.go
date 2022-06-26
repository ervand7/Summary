package main

import "fmt"

type Man struct {
	name   string
	age    int
	sex    string
	weight int
	height int
}

// NewMan constructor
func NewMan(name, sex string, age, weight, height int) Man {
	return Man{
		name:   name,
		sex:    sex,
		age:    age,
		weight: weight,
		height: height,
	}
}

func main() {
	man := NewMan("Vasya", "male", 25, 75, 185)
	fmt.Println(man) // {Vasya 25 male 75 185}
}
