package main

import "fmt"

/*
Копируется значение. Адреса разные. Поэтому, изменяя значение в `b`,
это не аффектит на `a`.
*/

func main() {
	a := "Hello"
	b := a

	b = "World"

	fmt.Println(a)
	fmt.Println(b)
}
