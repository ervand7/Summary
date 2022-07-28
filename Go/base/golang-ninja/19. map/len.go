package main

import "fmt"

func main() {
	users := map[string]int{
		"Vasya":  15,
		"Petya":  23,
		"Kostya": 48,
	}
	fmt.Println(len(users)) // 3
}
