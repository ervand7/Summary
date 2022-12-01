package append

import (
	"testing"
)

var data = []string{"medieval literature", "history", "design", "art", "choreography", "medieval literature", "history"}

func Benchmark_Allocation(b *testing.B) {
	for i := 0; i < b.N; i++ {
		var ll []string
		for _, l := range data {
			ll = append(ll, l)
		}
	}
}

func Benchmark_PreAllocation(b *testing.B) {
	for i := 0; i < b.N; i++ {
		ll := make([]string, 0, len(data))
		for _, l := range data {
			ll = append(ll, l)
		}
	}
}
