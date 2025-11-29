package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4}
	b := a[:2:2]
	c := append(b, 100)

	a[0] = 99

	fmt.Println("a:", a)
	fmt.Println("b:", b)
	fmt.Println("c:", c)
}
