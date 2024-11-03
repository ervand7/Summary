package main

import "fmt"

/*
Если бы мы объявили `arr := make([]int, 4, 5)` то получили бы совсем
другой результат:
[9 0 0 0]
[9 0 0 0 1]
так как append вернул бы тот же адрес памяти.
Вывод: результат append нужно присуждать тому же слайсу, который
мы и передаем в append.
*/

func main() {
	arr := make([]int, 4, 4)
	arr2 := append(arr, 1)
	fmt.Printf("%p\n", arr)  // 0x140000ba000
	fmt.Printf("%p\n", arr2) // 0x140000a8080

	arr[0] = 5
	arr2[0] = 9

	fmt.Println(arr)  // [5 0 0 0]
	fmt.Println(arr2) // [9 0 0 0 1]
}
