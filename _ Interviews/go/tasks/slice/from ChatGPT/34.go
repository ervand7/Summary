package main

import "fmt"

func change(x *[]int) {
	for i := 0; i < 3; i++ {
		*x = append(*x, i)
	}
}

func main() {
	s := make([]int, 0, 3)
	change(&s)
	fmt.Println(s)
}
