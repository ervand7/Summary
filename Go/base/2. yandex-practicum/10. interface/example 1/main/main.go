package main

import (
	"company"
	"fmt"
	"person"
	"robot"
)

func main() {
	comp := company.Company{}

	pers := person.Person{}
	robo := &robot.Robot{}

	comp.Hire(pers)
	fmt.Println(comp.Process(0, []string{"hello", "world"}))
	/*
		Person work:
		 I do hello
		 I do world
	*/

	comp.Hire(robo)
	fmt.Println(comp.Process(1, []string{"hello", "world"}))
	/*
		Robot  serialID 0 work:
		 I do hello
		 I do world
	*/
}
