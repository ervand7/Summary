package main

import "fmt"

func changeMapByDereferencing(m *map[int]int) {
	(*m)[1] = 777
}

func main() {
	m := map[int]int{1: 1, 2: 2}
	fmt.Println(m)

	changeMapByDereferencing(&m)
	fmt.Println(m)
}
