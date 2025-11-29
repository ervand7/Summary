package main

import "fmt"

func modify(s []int) {
	s = s[1:3]
	s[0] = 999
	s = append(s, 42)
}

func main() {
	a := []int{7, 8, 9, 10}
	modify(a)
	fmt.Println(a)
}
