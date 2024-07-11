package main

import "fmt"

func main() {
	var a = map[int]int{}
	b := a

	b[1] = 666
	fmt.Println(a)
	fmt.Println(b)
}
