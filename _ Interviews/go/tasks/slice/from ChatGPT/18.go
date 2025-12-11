package main

import "fmt"

func modify2(p *[]int) {
	*p = append(*p, 100)
}

func main() {
	a := make([]int, 0, 1)
	b := a
	modify2(&b)
	fmt.Println(a)
	fmt.Println(b)
}
