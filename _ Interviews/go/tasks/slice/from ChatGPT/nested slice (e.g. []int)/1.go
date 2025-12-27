package main

import "fmt"

func main() {
	a := [][]int{{1, 2}, {3, 4}}
	b := a
	b[0][0] = 9
	fmt.Println(a)
}
