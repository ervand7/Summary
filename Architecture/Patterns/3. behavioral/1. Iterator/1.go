package main

import "fmt"

/*
В простейшем случае для реализации Итератора можно использовать
замыкание (closure). Такой вариант бывает полезен при работе со счётчиком:
*/

func newEven() func() int {
	n := 0
	// функциональный литерал замкнёт переменную n
	return func() int {
		n += 2
		return n
	}
}

func main() {
	next := newEven()
	fmt.Println(next())
	fmt.Println(next())
	fmt.Println(next())
}

/*
2
4
6
*/
