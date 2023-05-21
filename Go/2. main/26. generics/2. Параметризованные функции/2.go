package main

import "fmt"

// Stringify На параметр T наложено ограничение интерфейса fmt.Stringer.
// []T — параметризованный тип,
// может быть слайсом любого типа, для которого реализован Stringer.
func Stringify[T fmt.Stringer](s []T) (ret []string) {
	for _, v := range s {
		// можно гарантированно вызвать метод String()
		ret = append(ret, v.String())
	}
	return ret
}
