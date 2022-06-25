package main

import "fmt"

var msg string

// always automatically runs before main() while package initialization
func init() {

	msg = "from init"
}

func main() {
	fmt.Println(msg)
	fmt.Println("Hello")
}
