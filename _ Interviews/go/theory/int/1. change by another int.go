package main

import "fmt"

/*
Копируется значение. Адреса разные. Поэтому, изменяя значение в `b`,
это не аффектит на `a`.
*/

func main() {
	a := 1
	b := a

	fmt.Printf("%p\n", &a) // 0x14000122008
	fmt.Printf("%p\n", &b) // 0x14000122010

	b = 777
	fmt.Printf("%p\n", &b) // 0x14000122010

	fmt.Println(a) // 1
	fmt.Println(b) // 777
}
