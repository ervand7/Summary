package main

import "fmt"

func grow(base []int) []int {
	base = append(base, 100)
	return base
}

func main() {
	s := []int{1, 2, 3}
	t := s[:2]
	t = grow(t)

	fmt.Println(s)
	fmt.Println(t)
}

