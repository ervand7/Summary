package main

import "fmt"

/*
мораль: итерация по строке идет посимвольно (по рунам), а не побайтово.
*/

func main() {
	var a = "qwerty"
	for _, val := range a {
		fmt.Println(val)
	}
	/*
		113
		119
		101
		114
		116
		121
	*/

	fmt.Println()

	var b = "йцукен"
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
}
