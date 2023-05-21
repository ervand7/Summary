package main

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

type Slice[T any] []T

func (s *Slice[T]) Map(f func(T) T) *Slice[T] {
	for k, v := range *s {
		(*s)[k] = f(v)
	}
	return s
}

// Double constraints.Ordered описывает строки, целые числа и числа
// с плавающей точкой. Для них точно определён оператор +
func Double[T constraints.Ordered](v T) T {
	return v + v
}

func main() {
	// надо конкретизировать тип Slice
	// нельзя декларировать переменную обобщённым типом
	var si = Slice[int]{1, 2, 3, 4, 5}
	// а здесь нужно конкретизировать функцию Double
	// её тоже не получится использовать в дженерик-форме
	si.Map(Double[int]).Map(Double[int])

	fmt.Println(si) // [4 8 12 16 20]

	// теперь для строк
	var ss = Slice[string]{"foo", "bar", "buzz"}
	// конкретизируем функцию
	DoubleStr := Double[string] // так тоже можно
	ss.Map(DoubleStr).Map(DoubleStr)

	fmt.Println(ss) // [foofoofoofoo barbarbarbar buzzbuzzbuzzbuzz]
}
