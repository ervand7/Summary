package main

import "fmt"

/*
Итерация по строке идет посимвольно (по рунам), а не побайтово.
*/

func main() {
	var a = "qwerty"
	for i, val := range a {
		fmt.Println(i, val)
	}
	/*
		0 113
		1 119
		2 101
		3 114
		4 116
		5 121
	*/

	fmt.Println()

	var b = "йцукен"
	fmt.Println(b[:]) // йцукен
	for i, val := range b {
		fmt.Println(i, val)
	}
	/*
		0 1081
		2 1094
		4 1091
		6 1082
		8 1077
		10 1085
	*/

	fmt.Printf("%c%c%c%c%c%c", 1081, 1094, 1091, 1082, 1077, 1085) // йцукен
}
