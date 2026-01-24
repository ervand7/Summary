package main

import "fmt"

func main() {
	// 1) assign new empty slice
	a := []string{"A", "B", "C", "D", "E"}
	a = []string{}
	fmt.Println(a, len(a), cap(a), a == nil) // [] 0 0 false

	// 2) assign new via make func
	a = []string{"A", "B", "C", "D", "E"}
	a = make([]string, 0)
	fmt.Println(a, len(a), cap(a), a == nil) // [] 0 0 false

	// 3) assign nil. This will release the underlying array to the garbage collector
	// (assuming there are no other references).
	a = []string{"A", "B", "C", "D", "E"}
	a = nil
	fmt.Printf("%p\n", a)                    // 0x0
	fmt.Println(a, len(a), cap(a), a == nil) // [] 0 0 true

	// 4) To keep the underlying array with data, slice the slice to zero length.
	a = []string{"A", "B", "C", "D", "E"}
	a = a[:0]
	fmt.Println(a, len(a), cap(a)) // [] 0 5
	// If the slice is extended again, the original data reappears.
	fmt.Println(a[:2]) // [A B]
}
