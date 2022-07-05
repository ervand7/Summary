package main

import "fmt"

func fact(n int) int {
	res := 1
	for i := 1; i < n+1; i++ {
		res *= i

	}
	return res
}

func factRecursive(n int) int {
	if n == 0 { // терминальная ветка — то есть условие выхода из рекурсии
		return 1
	} else { // рекурсивная ветка
		return n * factRecursive(n-1)
	}
}

func main() {
	fmt.Println(fact(7))          // 5040
	fmt.Println(factRecursive(7)) // 5040
}
