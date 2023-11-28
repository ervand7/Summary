package main

import "fmt"

/*
Изначальный слайс изменится, так как в функции handle мы работаем со
слайсом от слайса.
*/

func handle(arr []int) {
	arr = append(arr, 5)
}

func main() {
	a := []int{1, 2, 3, 4}
	fmt.Println(a) //  [1 2 3 4]

	handle(a[:1])
	fmt.Println(a) // [1 5 3 4]
}
