package main

import "fmt"

func main() {
	matrix := make([][]int, 10)
	for i := 0; i < 10; i++ {
		for j := 0; j < 10; j++ {
			matrix[j] = make([]int, 10)
			matrix[j][i] = i
		}
		fmt.Println(matrix[i])
	}
}
