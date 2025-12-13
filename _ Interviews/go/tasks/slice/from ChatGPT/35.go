package main

import "fmt"

func change2(x *[]int) {
	for i := 0; i < 4; i++ {
		*x = append(*x, i)
	}
}

func main() {
	s := make([]int, 0, 3)
	change2(&s)
	fmt.Println(s)
}
