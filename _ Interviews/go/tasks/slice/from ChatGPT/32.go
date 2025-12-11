package main

import "fmt"

func main() {
	a := []int{10, 20, 30, 40}
	b := a[1:3]
	c := append(b, 99)
	b[0] = 777
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
