package main

import "fmt"

func main() {
	messages := make([]string, 100, 150)
	fmt.Println(len(messages)) // 100
	fmt.Println(cap(messages)) // 150

	messages = append(messages, "101")
	fmt.Println(len(messages)) // 101
	fmt.Println(cap(messages)) // 150
}
