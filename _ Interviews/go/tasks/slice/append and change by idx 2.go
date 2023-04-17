package main

import "fmt"

/*
А если применим dereferencing, то изначальный слайс поменяется и от append тоже.
*/

func changeOneByDereferencing(slice *[]int) {
	*slice = append(*slice, 5)
	fmt.Printf("%p\n", *slice) // 0x14000130000

	(*slice)[1] = 0
	fmt.Println(*slice) // [0 0 2 3 4 5]
}

func main() {
	slice := make([]int, 0)
	fmt.Printf("%p\n", slice) // 0x14000130000
	slice = append(slice, 0, 1, 2, 3, 4)

	changeOneByDereferencing(&slice)
	fmt.Println(slice) // [0 0 2 3 4 5]
}
