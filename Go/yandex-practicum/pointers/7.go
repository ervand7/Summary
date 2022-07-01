package main

import "fmt"

func main() {
	var weekTemp = [7]int{5, 4, 6, 8, 11, 9, 5}
	for _, temp := range &weekTemp {
		fmt.Println(temp)
	}
	/*
		5
		4
		6
		8
		11
		9
		5
	*/
	fmt.Println(weekTemp) // [5 4 6 8 11 9 5]
}
