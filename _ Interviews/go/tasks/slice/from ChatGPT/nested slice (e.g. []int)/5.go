package main

import "fmt"

func main() {
	a := [][]int{{1}, {2}, {3}}
	b := a[:2]
	b[1][0] = 9
	fmt.Println(a)
}
