package main

import "fmt"

func main() {
	var strs []string
	initSliceByValue(strs)
	fmt.Println(strs) // [] (nil)
	initSliceByPointer(&strs)
	fmt.Println(strs) // [hello]
}

func initSliceByValue(strs []string) {
	strs = make([]string, 0)
	strs = append(strs, "hello")
}

func initSliceByPointer(strs *[]string) {
	*strs = make([]string, 0)
	*strs = append(*strs, "hello")
}
