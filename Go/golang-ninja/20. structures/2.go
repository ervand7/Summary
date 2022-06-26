package main

import "fmt"

type User struct {
	name   string
	age    int
	sex    string
	weight int
	height int
}

func main() {
	user1 := User{"Vasya", 23, "Male", 75, 185}
	user2 := User{"Petya", 31, "Male", 84, 197}
	fmt.Printf("%+v\n", user1)
	fmt.Printf("%+v\n", user2)
	/*
		{name:Vasya age:23 sex:Male weight:75 height:185}
		{name:Petya age:31 sex:Male weight:84 height:197}
	*/
}
