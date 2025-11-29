package main

import "fmt"

func main() {
	var a []int
	b := make([]int, 0)

	a = append(a, 1)
	b = append(b, 1)

	fmt.Println("a:", a, "len:", len(a), "cap:", cap(a))
	fmt.Println("b:", b, "len:", len(b), "cap:", cap(b))

	fmt.Println("a == nil?", a == nil)
	fmt.Println("b == nil?", b == nil)
}
