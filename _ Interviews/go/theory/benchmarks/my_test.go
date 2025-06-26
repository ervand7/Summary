package myte_test

// go test -bench=.

import "testing"

func MyFunc1(n int) int {
	// твоя первая реализация
	return n * 2
}

func MyFunc2(n int) int {
	// твоя вторая реализация
	return n << 1
}

func BenchmarkMyFunc1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = MyFunc1(42)
	}
}

func BenchmarkMyFunc2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		_ = MyFunc2(42)
	}
}

// goos: darwin
// goarch: amd64
// BenchmarkMyFunc1-8   	1000000000	         0.34 ns/op
// BenchmarkMyFunc2-8   	1000000000	         0.22 ns/op
