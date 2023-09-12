package main

import "fmt"

func main() {
	a := make([]int, 6)
	fmt.Printf("%p\n", a) // 0x14000020120
	for i := 0; i < len(a); i++ {
		a[i] = i
	}
	fmt.Println(len(a), cap(a)) // 6 6

	// обрезаем снизу и сверху (адрес изменится, так как обрезаем снизу)
	b := a[1:3]
	fmt.Printf("%p\n", b)       // 0x14000020128
	fmt.Println(len(b), cap(b)) // 2 5

	// обрезаем только сверху (адрес останется тем же)
	c := a[:3]
	fmt.Printf("%p\n", c)
	fmt.Println(len(c), cap(c)) // 3 6 // 0x14000020120

	// обрезаем только снизу (адрес изменится, так как обрезаем снизу)
	d := a[3:]
	fmt.Printf("%p\n", d)       // 0x14000020138
	fmt.Println(len(d), cap(d)) // 3 3
}
