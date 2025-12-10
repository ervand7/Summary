package main

import "fmt"

func main() {
	s := make([]int, 2, 4)
	s[0], s[1] = 1, 2
	t := append(s, 3)
	u := append(t, 4)
	fmt.Println(s)
	fmt.Println(t)
	fmt.Println(u)
}
