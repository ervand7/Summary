package main

import "fmt"

func main() {
	a := []int{10, 20, 30, 40, 50}
	b := a[1:4]
	b = append(b, 999)
	fmt.Println(a)
	fmt.Println(b)
}
