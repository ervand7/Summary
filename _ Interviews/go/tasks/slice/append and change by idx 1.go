package main

import "fmt"

/*
Несмотря на то, что slice в отличие от массива передается в функцию как ссылка,
и то, что мы работаем с одним и тем же адресом памяти, append не заафектит slice
в main. Однако изменение по индексу заафектит.
*/

func changeOne(slice []int) {
	fmt.Printf("%p\n", slice) // 0x14000130000
	slice = append(slice, 5)
	fmt.Printf("%p\n", slice) // 0x14000130000

	slice[1] = 0
	fmt.Println(slice) // [0 0 2 3 4 5]
}

func main() {
	slice := make([]int, 0)   // 0x1005107c0
	fmt.Printf("%p\n", slice) // 0x14000130000
	slice = append(slice, 0, 1, 2, 3, 4)
	fmt.Printf("%p\n", slice) // 0x14000130000

	changeOne(slice)
	fmt.Println(slice) // [0 0 2 3 4]
}
