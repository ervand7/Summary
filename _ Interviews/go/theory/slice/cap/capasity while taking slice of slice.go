package main

import "fmt"

func main() {
	a := make([]int, 6, 6)
	for i := 0; i < len(a); i++ {
		a[i] = i
	}
	fmt.Println(len(a), cap(a)) // 6 6

	b := a[1:3]
	fmt.Println(len(b), cap(b)) // 2 5
}