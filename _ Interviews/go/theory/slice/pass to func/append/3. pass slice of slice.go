package main

import "fmt"

func handle(arr []int) {
	arr = append(arr, 5)
}

func main() {
	a := []int{1, 2, 3, 4}
	handle(a[1:])
	handle(a[:1])
	handle(a[1:2])
	fmt.Println(a)
}
