package main

import "fmt"

func modify4(x []int) {
	for i := range x {
		x[i] = x[i] * 2
	}
	x = append(x, 100)
}

func main() {
	s := []int{1, 2, 3}
	modify4(s)
	fmt.Println(s)
}
