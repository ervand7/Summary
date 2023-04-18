package main

import "fmt"

/*
мораль: итерация по строке идет посимвольно, а не побайтово.
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
	for _, val := range b {
		fmt.Println(val)
	}
	/*
		1081
		1094
		1091
		1082
		1077
		1085
	*/
}
