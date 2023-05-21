package main

import "fmt"

func main() {
	users := map[string]int{
		"Vasya":  15,
		"Petya":  23,
		"Kostya": 48,
	}
	delete(users, "Vasya")

	for key, value := range users {
		fmt.Println(key, value)
	}
	/*
		Petya 23
		Kostya 48
	*/
}
