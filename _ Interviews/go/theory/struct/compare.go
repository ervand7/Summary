package main

import "fmt"

/*
Итог:
 - структуры одного типа (person) можно сравнивать друг с другом
 - соответственно, можно структуру использовать как ключ в мапе и по этому
 ключу проводить поиск
 - ссылки на структуры нельзя сравнивать, так как это разные адреса памяти
*/

type person struct {
	name string
	age  int
}

func main() {
	a := person{
		name: "Ivan",
		age:  10,
	}
	b := person{
		name: "Ivan",
		age:  10,
	}
	fmt.Println(a == b) // true

	m := map[person]int{person{name: "Ivan", age: 10}: 1}
	key := person{name: "Ivan", age: 10}
	val, ok := m[key]
	fmt.Println(val, ok) // 1 true

	fmt.Println(&a == &b) // false
}
