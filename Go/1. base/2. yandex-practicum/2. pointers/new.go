package main

import "fmt"

func main() {
	/*
		А ещё в Go есть встроенная функция new(). В качестве параметра
		ей передаётся тип (не переменная), а возвращается указатель на новую
		переменную соответствующего типа.
	*/
	type A struct {
		IntField int
	}

	p := new(A)    //  то же самое, что и &A{}
	fmt.Println(p) // &{0}
}
