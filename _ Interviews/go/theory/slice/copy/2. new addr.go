package main

import "fmt"

// создается слайс с другим адресом, соответственно с другим базовым массивом

func main() {
	var a = []int{1, 2, 3}
	var b = make([]int, len(a))
	copy(b, a)

	fmt.Printf("%p\n", a) // 0x14000114018
	fmt.Printf("%p\n", b) // 0x14000114030

	fmt.Println(b) // [1 2 3]
	a[0] = 777
	fmt.Println(b) // [1 2 3]
}
