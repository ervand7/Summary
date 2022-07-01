package main

import "fmt"

func main() {
	/*
		Для создания слайса используется встроенная функция make()
		mySlice := make([]TypeOfelement, LenOfslice, CapOfSlice)
	*/
	mySlice := make([]int, 5) // слайс [0 0 0 0 0], базовый массив [0 0 0 0 0]
	fmt.Println(mySlice)
	mySlice_ := make([]int, 5, 10) // слайс [0 0 0 0 0], базовый массив [0 0 0 0 0 0 0 0 0 0]
	fmt.Println(mySlice_)
}
