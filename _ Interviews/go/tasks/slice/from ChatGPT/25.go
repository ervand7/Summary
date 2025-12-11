package main

import "fmt"

func main() {
	s := make([]int, 0, 3)
	s = append(s, 1)
	t := append(s, 2)
	u := append(s, 3)
	fmt.Println(s)
	fmt.Println(t)
	fmt.Println(u)
}
