package main

import "fmt"

// map in go is not ordered
// Но, нужно знать, что функция Println сортирует мапу под капотом

func main() {
	m := map[int]string{
		1: "a",
		2: "b",
		3: "c",
		4: "d",
	}

	for k, v := range m {
		fmt.Println(k, v)
	}
	for k := range m {
		fmt.Println(k)
	}

	fmt.Println(m)
}