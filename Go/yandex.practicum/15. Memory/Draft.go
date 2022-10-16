package main

import "fmt"

func main() {
	a := []int{1, 2, 3}
	a = append(a, 5)
	fmt.Println(a)
}
