package main

import "fmt"

/*
Если обе структуры абсолютно одинаковы по составу полей, мы можем кастить.
Однако не понадобится кастить, если применяем анонимную структуру.
*/

type s1 struct {
	name string
	age  int8
}

type s2 struct {
	name string
	age  int8
}

func main() {
	var a s1
	var b s2

	// a = b // Cannot use 'b' (type s2) as the type s1
	a = s1(b)
	fmt.Printf("%#v", a) // main.s1{name:"", age:0}

	var anon struct {
		name string
		age  int8
	}
	a = anon // никакой ошибки нет
}
