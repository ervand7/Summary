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
func (s *SomeUsr) printUsrInfo(name string) {
	s.name = name
	fmt.Println(s.name, s.age, s.sex, s.weight, s.height)
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
