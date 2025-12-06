package main

import "fmt"

// передав map в другую функцию и там изменив его по ключу, map изменится везде

func changeMap(m map[int]int) {
	m[1] = 777
}

func main() {
	m := map[int]int{1: 1, 2: 2}
	fmt.Println(m)

	changeMap(m)
	fmt.Println(m)
}
