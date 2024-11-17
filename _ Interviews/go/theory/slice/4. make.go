package main

import "fmt"

func main() {
	// создастся слайс имеющий 100 дефолтных элементов и cap 100
	a := make([]int, 100)
	fmt.Println(len(a)) // 100
	fmt.Println(cap(a)) // 100

	a = append(a, 555)
	fmt.Println(len(a)) // 101
	fmt.Println(cap(a)) // 224
	fmt.Println(a)
	/*
	   [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
	   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
	   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 555]
	*/

	// создастся пустой слайс имеющий capacity 100
	b := make([]int, 0, 100)
	b = append(b, 555)
	fmt.Println(len(b)) // 1
	fmt.Println(cap(b)) // 100
	fmt.Println(b)      // [555]
}
