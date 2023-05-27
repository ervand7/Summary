package main

import "fmt"

type operateFunc[T any] func(t T) T

func operate[T any](slice []T, fn operateFunc[T]) []T {
	ret := make([]T, len(slice))
	for i, v := range slice {
		ret[i] = fn(v)
	}
	return ret
}

func Double(n []int) []int {
	fn := func(n int) int {
		return 2 * n
	}
	numbers := operate(n, fn)
	fmt.Printf("%T", numbers)
	return numbers
}

func main() {
	result := Double([]int{1, 2, 3})
	fmt.Println(result)
}
