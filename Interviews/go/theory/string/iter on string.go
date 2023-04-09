package main

import "fmt"

func main() {
	var a string = "qwerty"
	for _, val := range []byte(a) {
		fmt.Println(val)
	}
}

/*
113
119
101
114
116
121
*/
