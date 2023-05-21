package sort

import (
	"testing"
)

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

func Test_BubbleSort(t *testing.T) {
	out := []int{1, 2, 2, 3, 4, 4, 5}
	in := []int{1, 4, 2, 3, 2, 4, 5}

	got := bubbleSort(in)

	for i := range out {
		if out[i] != got[i] {
			t.Fatalf("expected sorted, got: %v", got)
		}
	}
}

func mergeSort(in []int) []int {
	l := len(in)
	if l == 1 {
		return in
	}

	mid := l / 2
	left := in[:mid]
	right := in[mid:] // make([]int, l-mid)

	return merge(mergeSort(left), mergeSort(right))
}

func merge(left, right []int) []int {
	result := make([]int, len(left)+len(right))

	i := 0
	for len(left) > 0 && len(right) > 0 {
		if left[0] < right[0] {
			result[i] = left[0]
			left = left[1:]
		} else {
			result[i] = right[0]
			right = right[1:]
		}
		i++
	}

	for j := 0; j < len(left); j++ {
		result[i] = left[j]
		i++
	}
	for j := 0; j < len(right); j++ {
		result[i] = right[j]
		i++
	}

	return result
}

func TestMergeSort(t *testing.T) {
	out := []int{1, 2, 2, 3, 4, 4, 5}
	in := []int{1, 4, 2, 3, 2, 4, 5}

	got := mergeSort(in)

	for i := range out {
		if out[i] != got[i] {
			t.Fatalf("expected sorted, got: %v", got)
		}
	}
}

func BenchmarkBubbleSort(b *testing.B) {
	g := generateSlice(10000)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		bubbleSort(g)
	}
}

func BenchmarkMerge(b *testing.B) {
	g := generateSlice(10000)
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		mergeSort(g)
	}
}
