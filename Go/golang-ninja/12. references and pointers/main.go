package main

import "fmt"

func main() {
	message := "hello"
	fmt.Println(message) // hello
	// make referencing
	changeMessage(&message)
	fmt.Println(message) // hello modified
}

func changeMessage(message *string) { // point, that we pass pointer
	// make dereferencing
	*message += " modified"
}
