package main

import "fmt"

func main() {
	users := map[string]int{
		"Vasya":  15,
		"Petya":  23,
		"Kostya": 48,
	}
	users["Serega"] = 21

	for key, value := range users {
		fmt.Println(key, value)
	}
	/*
		Vasya 15
		Petya 23
		Kostya 48
		Serega 21
	*/
}
