package main

import "fmt"

/*
Видим, что результат объявления структуры как это сделано в p1 и p2 - одинаковый.
То же самое если сравнивать p3 и p4.
Однако p1 != p3.
*/

type Person struct {
	Name  string
	Email string
}

func main() {
	p1 := Person{}        // main.Person{Name:"", Email:""}
	var p2 Person         // main.Person{Name:"", Email:""}
	fmt.Println(p1 == p2) // true

	p3 := Person{"Ivan", "qew@qwe.ru"}              // main.Person{Name:"Ivan", Email:"qew@qwe.ru"}
	p4 := Person{Name: "Ivan", Email: "qew@qwe.ru"} // main.Person{Name:"Ivan", Email:"qew@qwe.ru"}
	fmt.Println(p3 == p4)                           // true

	fmt.Println(p1 == p3) // false

	fmt.Printf("%#v\n", p1)
	fmt.Printf("%#v\n", p2)
	fmt.Printf("%#v\n", p3)
	fmt.Printf("%#v\n", p4)
}
