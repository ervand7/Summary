package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4, 5}
	b := a[1:3]
	c := append(b, 100, 200)
	b[0] = 999

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
