package main

import "fmt"

func main() {
	// 1) assign new empty slice
	a := []string{"A", "B", "C", "D", "E"}
	fmt.Printf("%p\n", a) // 0x140000ae000
	a = []string{}
	fmt.Printf("%p\n", a)                    // 0x10282afc8
	fmt.Println(a, len(a), cap(a), a == nil) // [] 0 0 false

	// 2) assign new via make func
	a = []string{"A", "B", "C", "D", "E"}
	fmt.Printf("%p\n", a) // 0x140000ae050
	a = make([]string, 0)
	fmt.Printf("%p\n", a)                    // 0x105022fc8
	fmt.Println(a, len(a), cap(a), a == nil) // [] 0 0 false

	// 3) assign nil. This will release the underlying array to the garbage collector
	// (assuming there are no other references).
	a = []string{"A", "B", "C", "D", "E"}
	fmt.Printf("%p\n", a) // 0x1400010c0f0
	a = nil
	fmt.Printf("%p\n", a)                    // 0x0
	fmt.Println(a, len(a), cap(a), a == nil) // [] 0 0 true

	// 4) To keep the underlying array with data, slice the slice to zero length.
	a = []string{"A", "B", "C", "D", "E"}
	fmt.Printf("%p\n", a) // 0x1400010c140
	a = a[:0]
	fmt.Printf("%p\n", a)          // 0x1400010c140
	fmt.Println(a, len(a), cap(a)) // [] 0 5
	// If the slice is extended again, the original data reappears.
	fmt.Println(a[:2]) // [A B]
}
