package main

import "fmt"

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
