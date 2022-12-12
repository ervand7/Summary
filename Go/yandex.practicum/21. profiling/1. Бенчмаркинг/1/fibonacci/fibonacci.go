package fibonacci

func FiboRecursive(n int) int {
	if n <= 1 {
		return n
	}
	return FiboRecursive(n-2) + FiboRecursive(n-1)
}

func FiboOptimized(n int) int {
	if n <= 1 {
		return n
	}
	fibo := make([]int, n+1)
	fibo[1] = 1
	for i := 2; i <= n; i++ {
		fibo[i] = fibo[i-2] + fibo[i-1]
	}
	return fibo[n]
}
