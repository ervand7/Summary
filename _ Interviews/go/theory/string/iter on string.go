package main

import "fmt"

func main() {
	var a = "qwerty"
	for _, val := range []byte(a) {
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
	for _, val := range []byte(b) {
		fmt.Println(val)
	}
	/*
		208
		185
		209
		134
		209
		131
		208
		186
		208
		181
		208
		189
	*/
}
