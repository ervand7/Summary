package main

import "fmt"

// передав map в другую функцию и там изменив его по ключу, map изменится везде

func changeMap(m map[int]int) {
	m[1] = 777
	fmt.Printf("%p\n", m) // 0x14000116030
	fmt.Println(m)        // map[1:777 2:2]

}

func main() {
	m := map[int]int{1: 1, 2: 2}
	fmt.Printf("%p\n", m) // 0x14000116030
	fmt.Println(m)        // map[1:1 2:2]

	changeMap(m)
	fmt.Printf("%p\n", m) // 0x14000116030
	fmt.Println(m)        // map[1:777 2:2]
}
