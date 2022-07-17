package main

import "fmt"

/*
Отложенных вызовов может быть несколько. Тогда они выполняются в
обратном порядке, то есть начиная с того, который был отложен последним,
так как вызовы складывались в стек.
*/
func main() {
	fmt.Println("Hello")
	for i := 1; i <= 3; i++ {
		defer fmt.Println(i)
	}
	fmt.Println("World")
}

/*
Hello
World
3
2
1
*/
