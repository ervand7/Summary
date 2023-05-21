package main

import "fmt"

func main() {
	/*
		Для указателей на структуры в Go есть возможность неявного
		разыменования при доступе к полям структуры
	*/
	type A struct {
		IntField int
	}

	p := &A{}
	p.IntField = 42
	fmt.Println(p.IntField) // 42
	// вместо
	fmt.Println((*p).IntField) // 42
}
