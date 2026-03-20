package main

import "fmt"

// in python the result would be completely different

func main() {
	a := make([]int, 10)
	b := a[:]

	b[0] = 777
	fmt.Println(a)
	fmt.Println(b)
}
