package main

import "fmt"

type Ordered interface {
	~int | ~int64 | ~float64 | ~string
}

func Min[T Ordered](a, b T) T {
	if a < b {
		return a
	}

	return b
}

func main() {
	result := Min(2, 4)

	fmt.Println(result)
}
