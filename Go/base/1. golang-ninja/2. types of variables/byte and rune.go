package main

import "fmt"

func main() {
	var myByte byte = 62
	fmt.Printf("%c\n", myByte)   // > (output accordance from the ASCII table)
	something := []byte("hello") // [104 101 108 108 111]
	fmt.Println(something)

	// rune - opposite operation of byte
	var a rune = '>' // single quotes
	fmt.Println(a)   // 62
}
