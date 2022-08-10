package main

import "fmt"

func Generate(seed int) func() {
	return func() {
		fmt.Println(seed) // замыкание получает внешнюю переменную seed
		seed += 2         // переменная модифицируется
	}

}

func main() {
	iterator := Generate(0)
	iterator()
	iterator()
	iterator()
	iterator()
	iterator()
}

/*
0
2
4
6
8
*/
