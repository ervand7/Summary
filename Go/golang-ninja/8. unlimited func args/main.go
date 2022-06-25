package main

import "fmt"

func main() {
	fmt.Println(findMin(1, 2, 3, 345, 4564, 567, -55))
}

func findMin(numbers ...int) int {
	if len(numbers) == 0 {
		return 0
	}
	min := numbers[0]

	for _, i := range numbers {
		if i < min {
			min = i
		}
	}
	return min
}
