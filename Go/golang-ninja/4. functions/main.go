package main

import "fmt"

func main() {
	printMessage("Hello")

	msg := sayHello("Иван", 15)
	fmt.Println(msg)
}

func printMessage(message string) {
	fmt.Println(message)
}

func sayHello(name string, age int) string {
	result := fmt.Sprintf("Привет, %s! Тебе %d лет", name, age)
	return result
}
