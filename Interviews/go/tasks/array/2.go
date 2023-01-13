package main

import "fmt"

func appender(arr []int) {
	arr = append(arr, 5)
	fmt.Printf("====3, %p\n", arr)
	arr[0] = 123
	fmt.Println(arr)
}

func main() {
	a := make([]int, 0)
	fmt.Printf("====1, %p\n", a)
	a = append(a, 0, 1, 2, 3, 4)
	fmt.Printf("====2, %p\n", a)
	fmt.Println(a)

	appender(a)
	fmt.Println(a)
}

/*
====1, 0x10425efc8
====2, 0x14000124030
[0 1 2 3 4]
====3, 0x14000124030
[123 1 2 3 4 5]
[123 1 2 3 4]
*/
