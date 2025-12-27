package main

import "fmt"

func main() {
	a := make([][]int, 2)
	row := []int{1, 2}

	for i := range a {
		a[i] = row
	}

	a[1][0] = 9
	fmt.Println(a)
}
