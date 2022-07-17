package main

import "fmt"

func unintuitive() (value string) {
	defer func() { value = "На самом деле" }()
	return "Казалось бы"
}

/*
Обратите внимание, это работает только с именованными возвращаемыми значениями.
Следующий код выведет "Казалось бы":
*/
func intuitive2() string {
	value := "Казалось бы"
	defer func() { value = "На самом деле" }()
	return value
}
func main() {
	fmt.Println(unintuitive()) // На самом деле
	fmt.Println(intuitive2())  // Казалось бы
}
