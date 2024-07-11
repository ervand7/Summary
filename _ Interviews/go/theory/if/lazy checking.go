package main

import "fmt"

/*
Функция incrementB() даже не отработает, так как первое условие уже верно.
И Из-за того, что функция не отработает, b не увеличится
*/

func main() {
	a, b := 1, 0

	incrementB := func() bool {
		b = b + 1
		fmt.Print("Hello")
		return true
	}

	if a == 1 || incrementB() {
		fmt.Println("World")
	}

	fmt.Println(a, b) // 1 0
}
