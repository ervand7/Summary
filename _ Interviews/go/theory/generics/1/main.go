package main

import (
	"fmt"

	"golang.org/x/exp/constraints"
)

// MaxNumber возвращает максимальное значение числового слайса.
func MaxNumber[T constraints.Integer | constraints.Float](slice []T) T {
	if len(slice) == 0 {
		// для пустого слайса возвращаем нулевое значение
		return 0
	}
	maximum := slice[0]
	for i := 1; i < len(slice); i++ {
		if slice[i] > maximum {
			maximum = slice[i]
		}
	}
	return maximum
}

func main() {
	fmt.Println("Max int32", MaxNumber([]int32{45, 678, -232, 0, 2}))
	fmt.Println("Max int64", MaxNumber([]int64{-2435, 243434, -5655, -1, 777}))
	fmt.Println("Max float32", MaxNumber([]float32{-1.56, 17, 6.78, 1024.782}))
}

/*
Max int32 678
Max int64 243434
Max float32 1024.782
*/
