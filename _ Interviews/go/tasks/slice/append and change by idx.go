package main

import "fmt"

/*
Несмотря на то, что slice в отличие от массива передается в функцию как ссылка,
и внутри этой функции мы будем работать с этим slice как со ссылкой,
append не заафектит slice в main. Однако изменение индекса заафектит.
*/

func changeOne(slice []int) {
	slice = append(slice, 5)
	fmt.Printf("%p\n", slice) // 0x14000130000

	slice[1] = 0
	fmt.Println(slice) // [0 0 2 3 4 5]
}

func main() {
	slice := make([]int, 0, 10)
	fmt.Printf("%p\n", slice) // 0x14000130000
	slice = append(slice, 0, 1, 2, 3, 4)

	changeOne(slice)
	fmt.Println(slice) // [0 0 2 3 4]
}
