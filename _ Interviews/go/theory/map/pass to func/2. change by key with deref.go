package main

import "fmt"

// тот же результат будет и с dereferencing

func changeMapByDereferencing(m *map[int]int) {
	(*m)[1] = 777
	fmt.Printf("%p\n", *m) // 0x1400018e030
	fmt.Println(*m)        // map[1:777 2:2]

}

func main() {
	m := map[int]int{1: 1, 2: 2}
	fmt.Printf("%p\n", m) // 0x1400018e030
	fmt.Println(m)        // map[1:1 2:2]

	changeMapByDereferencing(&m)
	fmt.Printf("%p\n", m) // 0x1400018e030
	fmt.Println(m)        // map[1:777 2:2]
}
