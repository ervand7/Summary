package main

// изменятся оба объекта

import "fmt"

func main() {
	a := []int{1, 2, 3}
	b := a
	fmt.Printf("%p\n", a) // 0x1400001e0f0
	fmt.Printf("%p\n", b) // 0x1400001e0f0

	b[0] = 777
	fmt.Println(a)        // [777 2 3]
	fmt.Println(b)        // [777 2 3]
	fmt.Printf("%p\n", a) // 0x1400001e0f0
	fmt.Printf("%p\n", b) // 0x1400001e0f0
}
