package main

import "fmt"

/*
Функция incB() даже не отработает, так как первое условие уже верно.
И Из-за того, что функция не отработает, b не увеличится
*/

func main() {
	a, b := 1, 0

	incB := func() bool {
		b = b + 1
		return true
	}

	if a == 1 || incB() {
		fmt.Println("Hello")
	}

	fmt.Println(a, b) // 1 0
}
