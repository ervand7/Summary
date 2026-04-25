package main

import "fmt"

func main() {
	arr := [5]int{1, 2, 3, 4, 5}
	s := arr[1:4]

	fmt.Println(s)      // [2 3 4]
	fmt.Println(len(s)) // 3
	fmt.Println(cap(s)) // 4
}
