package main

import "fmt"

// struct никогда не бывает nil

func main() {
	var a struct{}
	fmt.Println(a == struct{}{}) // true

	var a1 = struct{}{}
	fmt.Println(a1 == struct{}{}) // true

	a2 := struct{}{}
	fmt.Println(a2 == struct{}{}) // true

	type a3 struct{}
	fmt.Println(a3{} == struct{}{}) // true
}
