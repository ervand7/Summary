package main

import "fmt"

func main() {
	a := make([][]int, 2)
	for i := 0; i < 2; i++ {
		a[i] = make([]int, 2)
	}

	a[0][0] = 1
	b := a
	b[1][1] = 9

	fmt.Println(a)
}
