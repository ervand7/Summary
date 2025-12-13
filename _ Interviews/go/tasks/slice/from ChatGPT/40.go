package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4}
	a := s[1:3:3]
	a = append(a, 99)

	fmt.Println(s)
	fmt.Println(a)
}
