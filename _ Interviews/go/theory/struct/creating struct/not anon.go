package main

type Person struct {
	Name  string
	Email string
}

func main() {
	p1 := Person{}
	var p2 Person
	p3 := Person{"Ivan", "qew@qwe.ru"}
	p4 := Person{Name: "Ivan", Email: "qew@qwe.ru"}

	_, _, _, _ = p1, p2, p3, p4
}
