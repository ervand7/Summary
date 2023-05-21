package fibonacci

import "testing"

func BenchmarkFibo(b *testing.B) {
	count := 35
	b.Run("recursive", func(b *testing.B) {
		for i := 0; i < b.N; i++ {
			FiboRecursive(count)
		}
	})
	b.Run("optimized", func(b *testing.B) {
		for i := 0; i < b.N; i++ {
			FiboOptimized(count)
		}
	})
}
