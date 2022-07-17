package main

import "fmt"

func find(arr []int, k int) []int {
	m := make(map[int]int)
	for index, value := range arr {
		if j, ok := m[k-value]; ok {
			return []int{index, j}
		}
		m[value] = index
	}
	return nil
}
func main() {
	myArray := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	fmt.Println(find(myArray, 7)) // [3 2]
}

/*
 как можно заметить, алгоритм пройдётся по массиву всего один раз
 если бы мы искали подходящее значение каждый раз через перебор массива,
 то пришлось бы сделать гораздо больше вычислений
*/
