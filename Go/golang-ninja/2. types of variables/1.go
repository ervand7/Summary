package main

import "fmt"

func main() {
	// https://metanit.com/go/tutorial/2.3.php
	// null value in variables

	var message string
	fmt.Println(message) // empty string

	var number int
	var bit8intDefault int8
	fmt.Println(number)         // 0
	fmt.Println(bit8intDefault) // 0

	var myFloat float32
	fmt.Println(myFloat) // 0

	var myBool bool
	fmt.Println(myBool) // false
}
