package main

import (
	"fmt"
)

func main() {
	var a struct{}
	b := struct{}{}

	fmt.Println(a)      // {}
	fmt.Println(b)      // {}
	fmt.Println(a == b) // true
}
