package main

import "fmt"

/*
Массив передается в функцию как значение, а не как ссылка.
Поэтому он не изменится.
*/

func changeArr(arr [4]int) {
	arr[1] = 121212
}

func main() {
	arr := [4]int{}
	fmt.Println(arr) // [0 0 0 0]

	changeArr(arr)
	fmt.Println(arr) // [0 0 0 0]
}
