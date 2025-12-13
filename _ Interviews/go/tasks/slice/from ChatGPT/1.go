package main

import "fmt"

// Потому что все три append используют один и тот же подлежащий массив ёмкости 3,
// и каждая запись перезаписывает предыдущие позиции, поэтому все слайсы
// указывают на одни и те же данные.

func main() {
	s := make([]int, 0, 3)
	a := append(s, 1)
	b := append(s, 2)
	c := append(s, 3)
	fmt.Println(s)
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c)
}
