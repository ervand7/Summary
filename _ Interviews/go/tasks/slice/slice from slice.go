package main

import "fmt"

// оба слайса имеют один и тот же базовый массив, несмотря на разные адреса

func main() {
	a := []string{"x", "y", "z"}
	fmt.Printf("%p\n", a) // 0x1400010e180
	b := a[1:2]
	fmt.Printf("%p\n", b) // 0x1400010e190
	fmt.Println(b)        // [y]

	b[0] = "q"
	fmt.Println(a) // [x q z]
}
