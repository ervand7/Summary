package main

import "fmt"

func main() {
	s := "Привет!"
	fmt.Println(string([]rune(s)[2]))
}
