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

	/*
		мы передаём переменную типа Person в функцию,
		аргументом которой является переменная Worker
	*/
	comp.Hire(pers)
	comp.Hire(robo)
}
