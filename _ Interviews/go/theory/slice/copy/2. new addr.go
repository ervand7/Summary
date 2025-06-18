package main

import "fmt"

// создается слайс с другим адресом, соответственно с другим базовым массивом

func main() {
	var a = []int{1, 2, 3}
	var b = a[:0]

	fmt.Printf("%p\n", a)
	fmt.Printf("%p\n", b)

	c := b
	fmt.Println(c)
}
