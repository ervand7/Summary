package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := make([]int, 5)
	var c []int
	d := make([]int, 10)
	e := make([]int, 0, 10)

	copy(b, a)
	copy(c, a)
	copy(d, a)
	copy(e, a)

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
	fmt.Println(d)
	fmt.Println(e)
}
