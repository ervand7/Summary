package main

import "fmt"

func main() {
	rows := make([][]int, 0, 2)
	base := []int{1, 2, 3}
	rows = append(rows, base)
	rows = append(rows, base[:1])
	rows[0][0] = 99

	fmt.Println(rows)
}
