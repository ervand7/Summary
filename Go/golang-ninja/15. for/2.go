package main

import "fmt"

func main() {
	// My variant
	myMatrix := make([][]int, 10)
	for i := 0; i < 10; i++ {
		myMatrix[i] = make([]int, 10)
		myMatrix[i][i] = i
		fmt.Println(myMatrix[i])
	}
}
