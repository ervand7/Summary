package main

import "fmt"

/*
Видим, что результат объявления структуры как это сделано в p1 и p2 - одинаковый.
То же самое если сравнивать p3 и p4.
Однако p1 != p3, так как p1 - пустой, а p3 - нет.
*/

type Person struct {
	Name  string
	Email string
}

func main() {
	p1 := Person{}
	var p2 Person
	fmt.Println(p1 == p2) // true

	p3 := Person{"Ivan", "qew@qwe.ru"}
	p4 := Person{Name: "Ivan", Email: "qew@qwe.ru"}
	fmt.Println(p3 == p4) // true

	fmt.Println(p1 == p3) // false
}
