package main

import "fmt"

func main() {
	a := make([]int, 10)
	b := a[1 : len(a)-1]

	b = append(b, 1)
	fmt.Println(a)
	fmt.Println(b)
}
