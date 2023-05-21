package main

import "fmt"

func adder(s ...string) []string {
	var a []string
	a = append(a, s...)
	return a
}

func main() {
	fmt.Println(adder("hello", "world")) // [hello world]
}
