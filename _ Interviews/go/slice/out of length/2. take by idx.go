package main

import "fmt"

/*
Индекс связан с длиной, а не с capacity.
*/

func main() {
	var nums = make([]int, 0, 10)
	fmt.Println(nums[5]) // panic: runtime error: index out of range [5] with length 0
}
