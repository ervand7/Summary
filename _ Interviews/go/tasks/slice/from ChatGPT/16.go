package main

import "fmt"

func main() {
	s := []int{10, 20, 30, 40}
	t := s[:2:2]
	t = append(t, 99)
	fmt.Println(s)
	fmt.Println(t)
}
