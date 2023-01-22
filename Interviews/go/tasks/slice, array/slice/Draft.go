package main

import "fmt"

func main() {
	var strs []string
	initSliceByValue(strs) // []
	fmt.Println(strs)
	initSliceByPointer(&strs) // [hello]
	fmt.Println(strs)
}

func initSliceByValue(strs []string) {
	strs = make([]string, 0)
	strs = append(strs, "hello")
}

func initSliceByPointer(strs *[]string) {
	*strs = make([]string, 0)
	*strs = append(*strs, "hello")
}
