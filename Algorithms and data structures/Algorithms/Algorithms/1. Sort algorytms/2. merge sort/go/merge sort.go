package main

import (
	"fmt"
)

func rec(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}

	// Channels for left and right halves
	leftChan := make(chan []int)
	rightChan := make(chan []int)

	mid := len(nums) / 2

	// Launch goroutines to sort both halves concurrently
	go func() {
		leftChan <- rec(nums[:mid])
	}()
	go func() {
		rightChan <- rec(nums[mid:])
	}()

	// Receive sorted halves
	left := <-leftChan
	right := <-rightChan

	// Merge and return result
	return merge(left, right)
}

// merge merges two sorted slices into one sorted slice
func merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right))
	i, j := 0, 0

	// Merge step
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}

	// Append leftovers
	result = append(result, left[i:]...)
	result = append(result, right[j:]...)

	return result
}

func main() {
	nums := []int{5, 1, 1, 2, 0, 0}
	sorted := rec(nums)
	fmt.Println(sorted) // Output: [0 0 1 1 2 5]
}
