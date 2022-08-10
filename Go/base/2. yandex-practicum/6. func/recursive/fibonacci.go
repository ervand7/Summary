package main

import "fmt"

func Fib(n int) int {
	a, b := 0, 1
	for i := 0; i < n; i++ {
		a, b = b, a+b
	}
	return a
}

/* or:
func Fib(n int) int {
    a, b := 0, 1
    for n > 0 {
        a, b = b, a+b
        n--
    }
    return a
}
*/

func FibRecursive(n int) int {
	switch {
	case n <= 1: // терминальная ветка
		return n
	default: // рекурсивная ветка
		return FibRecursive(n-1) + FibRecursive(n-2)
	}
}

func main() {
	fmt.Println(Fib(42))          // 267914296
	fmt.Println(FibRecursive(42)) // 267914296
}
