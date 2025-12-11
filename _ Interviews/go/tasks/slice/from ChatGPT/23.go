package main

import "fmt"

func modify3(x []int) {
	for i := range x {
		x[i] = x[i] * 2
	}
	x = append(x, 100)
}

func main() {
	s := []int{1, 2, 3}
	modify3(s[1:2])
	fmt.Println(s)
}
