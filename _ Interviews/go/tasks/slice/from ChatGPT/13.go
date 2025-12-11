package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4, 5}
	x := s[:3]
	y := s[2:]
	copy(y, []int{9, 9, 9})
	fmt.Println(s)
	fmt.Println(x)
	fmt.Println(y)
}
