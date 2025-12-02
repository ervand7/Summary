package main

import "fmt"

func main() {
	s := []int{1, 2, 3}
	f := func(i int) any { return i * 2 }

	result := Map(s, f)
	fmt.Println(result)
}

func Map[T any, R any](s []T, f func(T) R) []R {
	var results = make([]R, 0, len(s))
	for _, v := range s {
		result := f(v)
		results = append(results, result)
	}

	return results
}
