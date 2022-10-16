package main

import "fmt"

func f(a []int) {
	a[1] = 5
}

func f2(a []int) {
	a = append(a, 5)
}

func main() {
	a := []int{1, 2, 3}
	f2(a)
	fmt.Println(a) // [1 2 3] - исходный слайс не изменился,
	// так как append возвращает новый объект

	f(a)
	fmt.Println(a) // [1 5 3] - исходный слайс изменился,
	// так как слайс переданный в функцию, передается как ссылка

	a = []int{1, 2, 3}
	b := a[:2:2] // сокращаем и len и cap
	f2(b)
	fmt.Println(b) // [1 2]
	fmt.Println(a) // [1 2 3]
}
