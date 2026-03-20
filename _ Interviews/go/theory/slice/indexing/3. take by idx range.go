package main

import "fmt"

// Индекс связан с длиной, а не с capacity.

func main() {
	var nums = make([]int, 0, 10)
	// fmt.Println(nums[5]) // panic: runtime error: index out of range [5] with length 0
	fmt.Println(nums[:])          // []
	fmt.Println(nums[3:7])        // [0 0 0 0]
	fmt.Println(nums[:cap(nums)]) // [0 0 0 0 0 0 0 0 0 0]

	a := make([]int, 1, 10)
	a[0] = 777
	fmt.Println(a[:])       // [777]
	fmt.Println(a[:cap(a)]) // [777 0 0 0 0 0 0 0 0 0]
}
