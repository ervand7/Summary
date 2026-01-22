package main

import "fmt"

func changeOne(slice []int) {
	slice = append(slice, 5)

	slice[1] = 0
	fmt.Println(slice)
}

func main() {
	slice := make([]int, 0)
	slice = append(slice, 0, 1, 2, 3, 4)

	changeOne(slice)
	fmt.Println(slice)
}
