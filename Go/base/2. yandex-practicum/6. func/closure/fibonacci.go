package main

import "fmt"

func fib() func() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

func main() {
	f := fib()       // получили функцию-замыкание. f() — захватила a, b. a = 0, b = 1
	fmt.Println(f()) // a = 1, b = 1
	fmt.Println(f()) // a = 1, b = 2
	fmt.Println(f()) // a = 2, b = 3
	fmt.Println(f()) // a = 3, b = 5
	fmt.Println(f()) // a = 5, b = 8
	fmt.Println(f()) // a = 8, b = 13
}
