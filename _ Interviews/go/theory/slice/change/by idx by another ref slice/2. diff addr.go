package main

import "fmt"

func main() {
	a := []int{1, 2, 3}
	b := a[1:2]

	b[0] = 777
	fmt.Println(a)
	fmt.Println(b)
}
