package main

import "fmt"

/*
У нас может быть много условий. И чтобы под каждое не писать отдельной
функции, можно передавать входящим аргументом анонимную функцию,
проверяющую соответствие условию.
*/

func findByCondition(slice []int, cond func(elem int) bool) []int {
	result := make([]int, 0, len(slice))
	for _, val := range slice {
		if cond(val) {
			result = append(result, val)
		}
	}

	return result
}

func main() {
	elements := []int{-5, 3, 0, 0, 20, -2, 4, 10, 0, -1, 4, -6, 7}
	cond := func(x int) bool {
		return x > 3
	}
	fmt.Println(findByCondition(elements, cond))
}
