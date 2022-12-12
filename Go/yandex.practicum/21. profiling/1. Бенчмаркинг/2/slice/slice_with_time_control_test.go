package slice

import (
	"math/rand"
	"sort"
	"testing"
	"time"
)

func BenchmarkSortSlice2(b *testing.B) {
	rand.Seed(time.Now().UnixNano())

	for i := 0; i < b.N; i++ {
		b.StopTimer() // останавливаем таймер
		slice := make([]int, 10000)
		for i := 0; i < len(slice); i++ {
			slice[i] = rand.Intn(1000)
		}
		b.StartTimer() // возобновляем таймер// сортируем
		sort.Slice(slice, func(i, j int) bool {
			return slice[i] < slice[j]
		})
	}
}
