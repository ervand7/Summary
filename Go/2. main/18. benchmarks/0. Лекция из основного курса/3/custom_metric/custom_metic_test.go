package custom_metric

import (
	"math/rand"
	"sort"
	"testing"
	"time"
)

func BenchmarkSortSlice(b *testing.B) {
	rand.Seed(time.Now().UnixNano())
	slice := make([]int, 10000)
	b.ResetTimer() // сбрасываем счётчик, чтобы инициализация слайса не посчиталась
	var cmps int64
	for i := 0; i < b.N; i++ {
		b.StopTimer() // останавливаем таймер
		for i := 0; i < len(slice); i++ {
			slice[i] = rand.Intn(1000)
		}
		b.StartTimer() // возобновляем таймер

		sort.Slice(slice, func(i, j int) bool {
			cmps++ // увеличиваем счётчик
			return slice[i] < slice[j]
		})
	}

	// добавляем метрику
	b.ReportMetric(float64(cmps)/float64(b.N), "compares/op")
}
