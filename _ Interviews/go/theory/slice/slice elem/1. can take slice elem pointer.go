package main

import "fmt"

func main() {
	a := []int{1, 2, 3}
	b := &a[0]
	fmt.Println(b) // 0x33c8e91580a8

	a = append(a, 4, 5, 6, 7, 8, 9, 10) // reallocation happened
	fmt.Println(b)                      // 0x33c8e91580a8
}
