package main

import "fmt"

// append will change initial slice if there will be enough capacity and len

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
