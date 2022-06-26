package main

import "fmt"

func main() {
	user := struct {
		name   string
		age    int
		sex    string
		weight int
		height int
	}{"Vasya", 23, "male", 75, 185}
	fmt.Println(user) // {Vasya 23 male 75 185}
	fmt.Printf("%+v\n", user)
}
