package main

import "fmt"

func main() {
	s := make([]int, 2, 2)
	s[0], s[1] = 1, 2

	p := &s[0]
	s = append(s, 3)
	s[0] = 10

	fmt.Println(*p, s)
}
