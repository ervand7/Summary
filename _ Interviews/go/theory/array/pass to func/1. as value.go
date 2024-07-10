package main

import "fmt"

/*
Массив передается в функцию как значение, а не как ссылка.
Поэтому он не изменится.
*/

func changeArr(arr [4]int) {
	fmt.Printf("%p\n", &arr) // 0x1400012a040 - другой адрес
	arr[1] = 121212
}

func main() {
	arr := [4]int{}
	fmt.Println(arr)         // [0 0 0 0]
	fmt.Printf("%p\n", &arr) // 0x1400012a000

	changeArr(arr)
	fmt.Println(arr) // [0 0 0 0]
}
