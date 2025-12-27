package main

import "fmt"

func main() {
	a := [][]int{{1, 2, 3}}
	b := a[0][:2]
	b[1] = 9
	fmt.Println(a)
}
