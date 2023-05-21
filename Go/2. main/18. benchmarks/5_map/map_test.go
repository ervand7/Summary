package t_test

import "testing"

func Benchmark_String(b *testing.B) {
	m := map[string]bool{
		"true": true,
	}
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		_ = m["true"]
	}
}

func Benchmark_Uint(b *testing.B) {
	m := map[uint]bool{
		10: true,
	}
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		_ = m[10]
	}
}
