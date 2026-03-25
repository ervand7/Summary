package main

import "fmt"

func change3(x *[]int) {
	for i := 0; i < 10; i++ {
		*x = append(*x, i)
	}
}

func main() {
	s := make([]int, 0, 3)
	change3(&s)
	fmt.Println(s)
}
