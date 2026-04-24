package main

import "fmt"

func modify5(p []int) {
	p = append(p, 100)
}

func main() {
	a := make([]int, 1)
	b := a[:0]
	modify5(b)
	fmt.Println(a)
	fmt.Println(b)
}
