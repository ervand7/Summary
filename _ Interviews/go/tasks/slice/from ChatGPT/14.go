package main

import "fmt"

func main() {
	a := make([]int, 2, 4)
	b := append(a, 10, 20)
	a[1] = 7
	b = append(b, 30)
	fmt.Println(a)
	fmt.Println(b)
}
