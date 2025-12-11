package main

import "fmt"

func modify(p *[]int) {
	*p = append(*p, 10)
}

func main() {
	s := []int{1, 2, 3}
	modify(&s)
	fmt.Println(s)
}
