package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4}

	b := a[:3]
	c := a[1:]
	d := append(b, 99)

	c[1] = 888

	fmt.Println("a:", a)
	fmt.Println("b:", b)
	fmt.Println("c:", c)
	fmt.Println("d:", d)
}
