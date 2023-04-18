package main

import "fmt"

// Слайс изменится. Все зависимости, применяем ли dereferencing или нет

func changeByIndex(arr []int) {
	arr[0] = 111
	fmt.Println(arr) // [111 1 2 3 4]
}

func main() {
	arr := []int{0, 1, 2, 3, 4}
	changeByIndex(arr)
	fmt.Println(arr) // [111 1 2 3 4]
}
