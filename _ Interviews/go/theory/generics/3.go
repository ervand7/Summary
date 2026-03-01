package main

import "fmt"

type Ordered interface {
	// `|` означает «или», а `~T` — любой тип с базовым типом `T`, например `~int` включает `int` и `type MyInt int`.
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
