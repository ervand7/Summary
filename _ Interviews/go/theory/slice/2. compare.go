package main

import (
	"fmt"
	"reflect"
	"slices"
)

func main() {
	// по дефолту в Go слайсы можно сравнивать только с nil
	a := []int{1, 2, 3}
	fmt.Println(a == nil) // false

	// можно использовать reflect.DeepEqual
	b := []int{1, 2, 3}
	fmt.Println(reflect.DeepEqual(a, b)) // true
	b = []int{1, 3, 2}
	fmt.Println(reflect.DeepEqual(a, b)) // false

	// лучше использовать package slices
	x := []byte{1, 2, 3}
	y := []byte{1, 2, 3}
	fmt.Println(slices.Equal(x, y)) // true

	// можно также проверить через цикл
	for i := 0; i < len(a); i++ {
		fmt.Println(a[i] == b[i])
	}
}
