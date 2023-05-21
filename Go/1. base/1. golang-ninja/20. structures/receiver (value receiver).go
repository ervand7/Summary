package main

import "fmt"

type MyUsr struct {
	name   string
	age    int
	sex    string
	weight int
	height int
}

// value receiver
func (m MyUsr) printUsrInfo(name string) {
	m.name = name
	fmt.Println(m.name, m.age, m.sex, m.weight, m.height)
}

func NewMyUsr(name, sex string, age, weight, height int) MyUsr {
	return MyUsr{
		name:   name,
		sex:    sex,
		age:    age,
		weight: weight,
		height: height,
	}
}

func main() {
	usr := NewMyUsr("Vasya", "male", 25, 75, 185)
	usr.printUsrInfo("Hello") // Hello 25 male 75 185
	fmt.Println(usr)          // {Vasya 25 male 75 185}
}
