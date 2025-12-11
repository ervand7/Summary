package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4}
	t := s[:2]
	t = append(t, 9)
	fmt.Println(s)
	fmt.Println(t)
}
