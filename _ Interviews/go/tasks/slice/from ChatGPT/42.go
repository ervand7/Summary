package main

import "fmt"

func main() {
	s := []int{1, 2, 3}
	t := append(s[:1], s...)

	fmt.Println(s)
	fmt.Println(t)
}
