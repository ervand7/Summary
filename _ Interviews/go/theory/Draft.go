package main

import "fmt"

func example() int {
	var result int
	defer func() {
		fmt.Println("defer runs")
		result = 100 // deferred function can modify named return values
	}()

	result = 5
	return result
}

func main() {
	fmt.Println(example())
}
