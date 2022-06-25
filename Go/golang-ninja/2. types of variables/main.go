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

	var myByte byte = 62
	fmt.Printf("%c\n", myByte)   // output accordance from the ASCII table
	something := []byte("hello") // [104 101 108 108 111]
	fmt.Println(something)

	var a rune = 'a'
	fmt.Println(a) // 97

}
