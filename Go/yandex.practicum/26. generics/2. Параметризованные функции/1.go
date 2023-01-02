package main

import "fmt"

// Print s — параметр параметризованного типа T
func Print[T any](s ...T) {
	for _, v := range s {
		fmt.Println(v)
	}
}

func main() {
	Print(1, 2, 3)
	Print("Hello", "Привет")
}
