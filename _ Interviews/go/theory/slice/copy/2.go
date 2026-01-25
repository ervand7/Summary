package main

import "fmt"

func main() {
	a := []int{1, 2, 3}
	b := a
	c := []int{7, 7, 7}
	copy(b, c[:2])

	b[0] = 777

	fmt.Println(a)
	fmt.Println(b)
}
