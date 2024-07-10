package main

import "fmt"

func main() {
	a := []byte("hello")
	fmt.Println(a) // [104 101 108 108 111]

	var b byte = 62
	fmt.Printf("%c\n", b) // > (output accordance from the ASCII table)

	// rune - opposite operation of byte
	var c rune = '>'
	fmt.Println(c) // 62
}
