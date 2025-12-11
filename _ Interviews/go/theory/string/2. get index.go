package main

import "fmt"

func main() {
	var a = "qwerty"
	fmt.Println(a[0])         // 113
	fmt.Println(string(a[0])) // q
	fmt.Printf("%c", 113)     // q
}
