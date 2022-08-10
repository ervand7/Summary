package main

import "fmt"

type SomeUsr struct {
	name   string
	age    int
	sex    string
	weight int
	height int
}

// pointer receiver
func (u *SomeUsr) printUsrInfo(name string) {
	u.name = name
	fmt.Println(u.name, u.age, u.sex, u.weight, u.height)
}

func NewSomeUsr(name, sex string, age, weight, height int) SomeUsr {
	return SomeUsr{
		name:   name,
		sex:    sex,
		age:    age,
		weight: weight,
		height: height,
	}
}

func main() {
	usr := NewSomeUsr("Vasya", "male", 25, 75, 185)
	usr.printUsrInfo("Hello") // Hello 25 male 75 185
	fmt.Println(usr)          // {Hello 25 male 75 185}
}
