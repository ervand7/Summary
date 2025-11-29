package main

import "fmt"

/*
 - слайс "a" не изменился потому, что в функции double ему был присвоен адрес
другого слайса и все изменения уже происходили с другим слайсом
 - слайс "b" был изменен, так как внутри функции double пыл произведен
dereferencing
*/

func double(alfa []int, beta *[]int) {
	newArr := []int{10, 11, 12}
	alfa = newArr
	for i := 0; i < len(alfa); i++ {
		alfa[i] *= 2
	}

	*beta = newArr
	for i := 0; i < len(*beta); i++ {
		(*beta)[i] *= 2
	}
}

func main() {
	a := []int{1, 2, 3}
	b := []int{4, 5, 6}

	double(a, &b)
	fmt.Println(a) // [1 2 3]
	fmt.Println(b) // [40 44 48]
}
