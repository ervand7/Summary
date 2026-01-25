package main

import "fmt"

/*
Индекс связан с длиной, а не с capacity.
*/

func main() {
	var nums []int
	fmt.Println(nums == nil, len(nums)) // true 0

	arr := make([]string, 1, 2)
	arr[0] = "hello"
	arr[1] = "world" // panic: runtime error: index out of range [2] with length 1
}
