package main

import "fmt"

func modify6(x []int) {
	for i := range []int{1, 2, 3} {
		x = append(x, i)
	}
}

func main() {
	s := make([]int, 3)
	modify6(s[:0])
	fmt.Println(s)
}
