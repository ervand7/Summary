package main

import "fmt"

var Global = 5

func main() {

	defer fmt.Println(Global)
	Global++
	fmt.Println("Changed: ", Global)
}
