package main

import "fmt"

/*
Дан массив целых чисел A и целое число k. Нужно найти и вывести индексы
пары чисел, сумма которых равна k. Если таких чисел нет, то вернуть
пустой слайс. Индексы можно вернуть в любом порядке.
*/
func main() {
	myArray := [10]int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	k := 7
	found := false
	for i := range myArray {
		for j := range myArray {
			if i != j {
				if myArray[i]+myArray[j] == k {
					found = true
					fmt.Println(i, j)
				}
			}
		}
	}
	if found == false {
		fmt.Println([]int{})
	}
	/*
		0 5
		1 4
		2 3
		3 2
		4 1
		5 0
	*/
}
