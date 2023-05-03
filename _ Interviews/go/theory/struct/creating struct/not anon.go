package main

import "fmt"

type Person struct {
	Name  string
	Email string
}

func main() {
	p1 := Person{}                                  // main.Person{Name:"", Email:""}
	var p2 Person                                   // main.Person{Name:"", Email:""}
	p3 := Person{"Ivan", "qew@qwe.ru"}              // main.Person{Name:"Ivan", Email:"qew@qwe.ru"}
	p4 := Person{Name: "Ivan", Email: "qew@qwe.ru"} // main.Person{Name:"Ivan", Email:"qew@qwe.ru"}

	fmt.Printf("%#v\n", p1)
	fmt.Printf("%#v\n", p2)
	fmt.Printf("%#v\n", p3)
	fmt.Printf("%#v\n", p4)
}
