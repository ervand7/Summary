package main

import "fmt"

func main() {
	a := []int{1, 2, 3, 4}
	b := a[:2]

	b = append(b, 10)
	a[1] = 99

	fmt.Println("a:", a)
	fmt.Println("b:", b)
}
