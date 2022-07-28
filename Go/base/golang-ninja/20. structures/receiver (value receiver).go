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
func (u MyUsr) printUsrInfo(name string) {
	u.name = name
	fmt.Println(u.name, u.age, u.sex, u.weight, u.height)
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
