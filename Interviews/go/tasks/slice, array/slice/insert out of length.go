package main

import "fmt"

func main() {
	var nums []int
	fmt.Println(nums == nil, len(nums)) // true 0

	strs := make([]string, 1, 2)
	strs[0] = "hello"
	strs[1] = "world" // panic: runtime error: index out of range [2] with length 1
}
