package main

// изменятся оба объекта. Разные адреса, но один и тот же базовый массив

import "fmt"

func main() {
	a := []int{1, 2, 3}
	b := a[1:2]
	fmt.Println(a)        // [1 2 3]
	fmt.Println(b)        // [2]
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130008

	b[0] = 777
	fmt.Println(a)        // [1 777 3]
	fmt.Println(b)        // [777]
	fmt.Printf("%p\n", a) // 0x14000130000
	fmt.Printf("%p\n", b) // 0x14000130008
}
