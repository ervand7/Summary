package main

import "fmt"

func main() {
	sum := Reduce(
		[]int{1, 2, 3},
		0,
		func(acc, v int) int { return acc + v },
	)

	fmt.Println(sum)
}

func Reduce[T any, R any](s []T, init R, f func(R, T) R) R {
	for _, v := range s {
		init = f(init, v)
	}

	return init
}
