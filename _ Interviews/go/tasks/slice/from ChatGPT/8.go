package main

import "fmt"

func main() {
	s := []int{1, 2, 3}
	t := append(s[:1], 10)
	u := append(s, 20)
	fmt.Println(s)
	fmt.Println(t)
	fmt.Println(u)
}
