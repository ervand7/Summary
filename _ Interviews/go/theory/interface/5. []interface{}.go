package main

import "fmt"

// В Go с помощью []interface{} можно сделать слайс, содержащий разные типы данных

func main() {
	a := []any{1, "Hello", true, map[int]int{1: 1}}
	a = append(a, []string{"qwe", "rty"})
	var x interface{}
	a = append(a, x)
	fmt.Println(a) // [1 Hello true map[1:1] [qwe rty] <nil>]
}
