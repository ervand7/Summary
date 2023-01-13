package main

import "fmt"

/*
Мораль такова: если передаем array в другую функцию, то
 - append в функции changeOne не заафектит array в main
 - изменения индекса заафектят
Здесь мы передаем array не как pointer, поэтому внутри функции changeOne
создается копия.
*/

func changeOne(arr []int) {
	arr[0] = 11111
	arr = append(arr, 5)
	arr[1] = 22222
	fmt.Println(arr) // [11111 22222 2 3 4 5]
}

func main() {
	arr := make([]int, 0)
	arr = append(arr, 0, 1, 2, 3, 4)

	changeOne(arr)
	fmt.Println(arr) // [11111 22222 2 3 4]
}
