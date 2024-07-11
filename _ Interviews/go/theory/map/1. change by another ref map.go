package main

import "fmt"

/*
Если присвоить одной мапе значение другой, и в другой что-то поменять
или добавить, то первая мапа тоже изменится.
Так как после присвоения вторая мапа получает адрес первой.
*/

func main() {
	m1 := make(map[string]string, 5)
	m2 := m1
	fmt.Printf("%p\n", m1) // 0x14000090180
	fmt.Printf("%p\n", m2) // 0x14000090180

	m2["hello"] = "world"

	fmt.Println(m1) // map[hello:world]
	fmt.Println(m2) // map[hello:world]
}
