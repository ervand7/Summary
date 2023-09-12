package main

import (
	"bytes"
	"fmt"
	"reflect"
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

	// однако, если это []byte, то в Go есть для этого встроенное сравнение
	x := []byte{1, 2, 3}
	y := []byte{1, 2, 3}
	fmt.Println(bytes.Equal(x, y)) // true

	// поэтому легче всего проверить через цикл
	for i := 0; i < len(a); i++ {
		fmt.Println(a[i] == b[i])
	}
}
