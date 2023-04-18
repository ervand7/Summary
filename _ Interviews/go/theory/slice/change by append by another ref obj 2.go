package main

import "fmt"

func main() {
	a := make([]int, 6, 6)
	for i := 0; i < len(a); i++ {
		a[i] = i
	}

	b := a[1:3]
	fmt.Println(a)        // [0 1 2 3 4 5]
	fmt.Println(b)        // [1 2]
	fmt.Printf("%p\n", a) // 0x14000124030
	// тут другой адрес, так как слайс обрезается снизу
	fmt.Printf("%p\n", b) // 0x14000124038

	// однако из-за того, что базовый массив один и тот же, оба поменяются
	b = append(b, 121212121)
	fmt.Println(a) // [0 1 2 121212121 4 5]
	fmt.Println(b) // [1 2 121212121]
}
