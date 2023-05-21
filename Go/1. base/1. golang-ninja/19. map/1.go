package main

import "fmt"

func main() {
	users := map[string]int{
		"Vasya":  15,
		"Petya":  23,
		"Kostya": 48,
	}
	fmt.Println(users["Vasya"])      // 15
	fmt.Println(users["Not exists"]) // 0

	age, exists := users["Kostya"]
	if exists {
		fmt.Println("Kostya", age)
	} else {
		fmt.Println("Kostya нет в списке")
	}
}
