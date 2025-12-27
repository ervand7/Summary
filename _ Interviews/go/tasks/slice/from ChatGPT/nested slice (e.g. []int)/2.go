package main

import "fmt"

func main() {
	a := [][]int{{1, 2}}
	b := append(a, []int{3, 4})
	a[0][1] = 8
	fmt.Println(b)
}
