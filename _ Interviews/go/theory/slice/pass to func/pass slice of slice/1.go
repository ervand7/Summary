package main

import "fmt"

/*
Изначальный слайс изменится, но только в том случае, если он обрезан сверху, а не снизу.
Это нужно запомнить.
*/

func handle(arr []int) {
	arr = append(arr, 5)
}

func main() {
	a := []int{1, 2, 3, 4}
	fmt.Println(a) //  [1 2 3 4]

	handle(a[1:])
	fmt.Println(a) //  [1 2 3 4]

	handle(a[:1])
	fmt.Println(a) // [1 5 3 4]
}
