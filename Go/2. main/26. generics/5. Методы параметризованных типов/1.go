package main

// Для параметризованного типа можно писать методы:

type VectorInt[T ~int | ~int8 | ~int16 | ~int32 | ~int64] []T

func (v VectorInt[T]) Sum() (t T) {
	for _, val := range v {
		t += val
	}
	return
}
