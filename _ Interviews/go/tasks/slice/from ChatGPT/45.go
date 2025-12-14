package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4}
	u := s[1:]
	s = append(s[:2], 9)

	fmt.Println(u)
	fmt.Println(s)
}

