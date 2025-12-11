package main

import "fmt"

func f(x []int) {
	for i := range x {
		x = append(x, i)
	}
}

func main() {
	s := make([]int, 0, 3)
	f(s)
	fmt.Println(s)
}
