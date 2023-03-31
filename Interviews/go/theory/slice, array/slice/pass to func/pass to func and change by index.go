package main

import "fmt"

/*
Мы можем передавать arr как value, и при этом изменение по индексу изменит
сам arr и это мы видим в main
*/

func changeByIndex(arr []int) {
	arr[0] = 111
	fmt.Println(arr) // [111 1 2 3 4]
}

func main() {
	arr := []int{0, 1, 2, 3, 4}

	changeByIndex(arr) // [111 1 2 3 4]
	fmt.Println(arr)   // [111 1 2 3 4]
}
