package slice

import (
	"math/rand"
	"sort"
	"testing"
	"time"
)

func BenchmarkSortSlice(b *testing.B) {
	rand.Seed(time.Now().UnixNano())

	for i := 0; i < b.N; i++ {
		slice := make([]int, 10000)
		// предзаполняем слайс
		for i := 0; i < len(slice); i++ {
			slice[i] = rand.Intn(1000)
		}

		// сортируем
		sort.Slice(slice, func(i, j int) bool {
			return slice[i] < slice[j]
		})
	}
}
