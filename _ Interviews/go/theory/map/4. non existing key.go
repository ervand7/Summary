package main

import "fmt"

/*
Можно обращаться к несуществующему ключу мапы и тогда получим нулевое значение
*/

func main() {
	m1 := make(map[int]int)
	fmt.Println(m1[777]) // 0
}
