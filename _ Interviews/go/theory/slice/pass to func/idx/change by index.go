package main

import "fmt"

func changeByIndex(arr []int) {
	arr[0] = 111
}

func main() {
	arr := []int{0, 1, 2, 3, 4}
	changeByIndex(arr)
	fmt.Println(arr)
}
