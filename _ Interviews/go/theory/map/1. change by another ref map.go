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

	m2["hello"] = "world"

	fmt.Println(m1)
	fmt.Println(m2)
}
