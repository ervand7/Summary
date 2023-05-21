package main

import "fmt"

func main() {
	matrix := make([][]int, 10)
	counter := 0
	for i := 0; i < 10; i++ {
		matrix[i] = make([]int, 10)

		for j := 0; j < 10; j++ {
			matrix[i][j] = counter
			counter++
		}
		fmt.Println(matrix[i])
	}
}
