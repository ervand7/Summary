package main

import (
	"company"
	"person"
	"robot"
)

func main() {
	comp := company.Company{}

	pers := person.Person{}
	robo := &robot.Robot{}

	comp.Hire(pers)
	comp.Hire(robo)
}
