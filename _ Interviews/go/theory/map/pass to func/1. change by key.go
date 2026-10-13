package main

import "fmt"

func changeMap(m map[int]int) {
	m[1] = 777
}

func main() {
	m := map[int]int{1: 1, 2: 2}
	fmt.Println(m)

	changeMap(m)
	fmt.Println(m)
}
