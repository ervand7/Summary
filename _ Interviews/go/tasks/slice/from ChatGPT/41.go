package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4}
	head := s[:0]
	head = append(head, 7)

	fmt.Println(s)
	fmt.Println(head)
}
