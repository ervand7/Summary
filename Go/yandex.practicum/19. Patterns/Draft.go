package main

import "fmt"

func main() {
	var a []int
	a = append(a, 1)
	fmt.Println(a)

	/*
		var b map[int]int
		b[1] = 1 // panic: assignment to entry in nil map
	*/
}
