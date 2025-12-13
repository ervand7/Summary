package main

import "fmt"

func main() {
	s := []int{1, 2, 3, 4}
	copy(s[1:], s[2:])
	fmt.Println(s)
}
