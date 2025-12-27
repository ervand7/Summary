package main

import "fmt"

func main() {
	a := [][]int{{1}, {2}}
	for i := range a {
		a[i] = append(a[i], i)
	}
	fmt.Println(a)
}
