package main

import "fmt"

func main() {
	messages := []string{
		"message 1",
		"message 2",
		"message 3",
		"message 4",
	}

	for index, message := range messages {
		fmt.Println(index, message)
	}
}
