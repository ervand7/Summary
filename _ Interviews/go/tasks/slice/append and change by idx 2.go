package main

import "fmt"

func changeOneByDereferencing(slice *[]int) {
	*slice = append(*slice, 5)
	(*slice)[1] = 0
}

func main() {
	slice := make([]int, 0)
	slice = append(slice, 0, 1, 2, 3, 4)

	changeOneByDereferencing(&slice)
	fmt.Println(slice)
}
