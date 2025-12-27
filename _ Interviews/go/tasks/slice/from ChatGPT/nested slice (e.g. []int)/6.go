package main

import "fmt"

func main() {
	a := [][]int{{1, 2}}
	b := append(a[0], 3)
	a[0][0] = 9
	fmt.Println(b)
}
