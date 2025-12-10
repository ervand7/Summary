package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4}
	t := s[1:3]
	t = append(t, 8, 9)
	fmt.Println(s)
	fmt.Println(t)
}
