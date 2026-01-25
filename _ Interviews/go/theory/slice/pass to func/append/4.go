package main

import "fmt"

func initSliceByValue(strs []string) {
	strs = make([]string, 0)
	strs = append(strs, "hello")
}

func initSliceByPointer(strs *[]string) {
	*strs = make([]string, 0)
	*strs = append(*strs, "hello")
}

func main() {
	var strs []string
	initSliceByValue(strs)
	fmt.Println(strs)
	initSliceByPointer(&strs)
	fmt.Println(strs)
}
