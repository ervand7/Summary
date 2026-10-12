package main

import "fmt"

// because after the second append we exceed the capacity

func ChangeOne(slice []int) {
	slice = append(slice, 5, 4)

	slice[1] = 0
	fmt.Println(slice)
}

func main() {
	slice := make([]int, 0)
	slice = append(slice, 0, 1, 2, 3, 4)

	ChangeOne(slice)
	fmt.Println(slice)
}
