package main

import "fmt"

type Usr struct {
	name   string
	age    int
	sex    string
	weight int
	height int
}

// receiver
func (u Usr) printUsrInfo() {
	fmt.Println(u.name, u.age, u.sex, u.weight, u.height)
}

func NewUsr(name, sex string, age, weight, height int) Usr {
	return Usr{
		name:   name,
		sex:    sex,
		age:    age,
		weight: weight,
		height: height,
	}
}

func main() {
	usr := NewUsr("Vasya", "male", 25, 75, 185)
	usr.printUsrInfo() // Vasya 25 male 75 185
}
