package sort

import "testing"

type numbers interface {
	int | int8 | int16 | int32 | int64 | float32 | float64
}

func genericBubbleSort[T numbers](in []T) []T {
	n := len(in)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if in[i] < in[j] {
				tmp := in[i]
				in[i] = in[j]
				in[j] = tmp
			}
		}
	}
	return in
}

func bubbleSort(in []int) []int {
	n := len(in)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if in[i] < in[j] {
				tmp := in[i]
				in[i] = in[j]
				in[j] = tmp
			}
		}
	}
	return in
}

func Benchmark_Bubble(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = bubbleSort([]int{1, 2, 3, 4, 11, 10, 23, 4, 7, 12, 55, 120, 77, 1, 12, 90, 55, 13, 44})
	}
}

func Benchmark_Generic(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = genericBubbleSort([]int64{1, 2, 3, 4, 11, 10, 23, 4, 7, 12, 55, 120, 77, 1, 12, 90, 55, 13, 44})
	}
}
