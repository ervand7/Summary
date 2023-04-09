package main

import "fmt"

func main() {
	var a [4]int
	fmt.Println(a, len(a) == 4) // [0 0 0 0] true

	b := [4]int{}
	fmt.Println(b, len(b) == 4) // [0 0 0 0] true
}
