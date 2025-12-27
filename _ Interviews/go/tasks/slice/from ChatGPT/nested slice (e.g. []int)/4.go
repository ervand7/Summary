package main

import "fmt"

func main() {
	a := [][]int{{1, 2}, {3, 4}}
	for _, row := range a {
		row[0] = 0
	}
	fmt.Println(a)
}
