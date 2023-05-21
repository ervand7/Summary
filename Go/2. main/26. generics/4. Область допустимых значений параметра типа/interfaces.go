package main

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

type StringerFloat interface {
	~float32 | ~float64
	String() string
}

// то же самое в другой записи
type StringerFloat2 interface {
	constraints.Float
	fmt.Stringer
}

/*
Такие интерфейсы, ограничивающие тип данных, можно применять для
квалификации параметров в списке type foo[T ConstraintInterface, ...],
но нельзя для декларации переменных var foo ConstraintInterface.
*/
