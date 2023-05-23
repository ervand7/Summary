package main

import (
	"errors"
	"fmt"
)

type vector[T any] []T

func (v vector[T]) last() (T, error) {
	var zero T
	if len(v) == 0 {
		return zero, errors.New("empty")
	}
	return v[len(v)-1], nil
}

func main() {
	a := vector[int]{1, 2, 3}
	fmt.Println(a.last()) // 3 <nil>

	b := vector[string]{"Hello", "World"}
	fmt.Println(b.last()) // World <nil>
}
