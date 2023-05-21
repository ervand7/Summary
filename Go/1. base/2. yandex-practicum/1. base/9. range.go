package main

import "fmt"

func main() {
	var weekTemp = [7]int{5, 4, 6, 8, 11, 9, 5}
	sumTemp := 0
	for _, temp := range weekTemp {
		sumTemp += temp
	}

	average := sumTemp / len(weekTemp)
	fmt.Println(average) // 6

	// если значение элемента не используется, можно опустить вторую переменную
	for i := range weekTemp {
		// в i будет индекс
		fmt.Println(i)
	}
	/*
		0
		1
		2
		3
		4
		5
		6
	*/
}
