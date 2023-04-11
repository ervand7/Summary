package main

import "fmt"

func double(alfa []int, beta *[]int) {
	newArr := []int{10, 11, 12}
	alfa = newArr
	fmt.Printf("%p\n", newArr) // 0x14000126030
	fmt.Printf("%p\n", alfa)   // 0x14000126030
	for i := 0; i < len(alfa); i++ {
		alfa[i] *= 2
	}
	*beta = newArr
	for i := 0; i < len(*beta); i++ {
		(*beta)[i] *= 2
	}
}

func main() {
	a := []int{1, 2, 3} // [1 2 3]
	b := []int{4, 5, 6} // [40 44 48]
	double(a, &b)
	fmt.Println(a, b)
}
