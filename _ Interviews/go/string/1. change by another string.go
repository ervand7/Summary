package main

import "fmt"

/*
Копируется значение. Адреса разные. Поэтому, изменяя значение в `b`,
это не аффектит на `a`.
*/

func main() {
	a := "Hello"
	b := a

	fmt.Printf("%p\n", &a) // 0x14000110210
	fmt.Printf("%p\n", &b) // 0x14000110220

	b = "World"
	fmt.Printf("%p\n", &b) // 0x14000110220

	fmt.Println(a) // Hello
	fmt.Println(b) // World
}
