package main

import "fmt"

func change4(x *[]int) {
	for i := 0; i < 3; i++ {
		*x = append(*x, i)
	}
}

func main() {
	s := make([]int, 0)
	change4(&s)
	fmt.Println(s)
}
