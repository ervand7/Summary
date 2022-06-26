package main

import "fmt"

func main() {
	defer handlePanic()

	messages := []string{
		"message 1",
		"message 2",
		"message 3",
		"message 4",
	}
	messages[4] = "message 5" // panic will be here

	fmt.Println(messages) // will not output
}

func handlePanic() {
	if r := recover(); r != nil {
		fmt.Println(r)
	}

	fmt.Println("handlePanic was completed successfully")
}
