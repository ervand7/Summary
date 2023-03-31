package main

import "fmt"

/*
defer возвращает то значение переменной,
которое у нее было на момент объявления defer.

Но, если вызвать эту переменную через defer + func, то мы получим последнее
значение этой переменной
*/

func main() {
	i := 0
	defer func() {
		fmt.Println(i)
	}()

	i += 3
	fmt.Println(i)

	i += 1
}

/*
3
4
*/
