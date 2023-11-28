package main

import "fmt"

/*
defer возвращает то значение переменной, которое у нее было на момент
объявления defer
*/

func main() {
	i := 0
	defer fmt.Println(i)

	i += 3
	fmt.Println(i)

	i += 1
}

/*
3
0
*/
