package main

import "fmt"

type A struct {
	a [][]string
	b []string
}

// when copying slices with nested slices, the nested ones remain with the same addresses

func main() {
	a1 := A{
		a: [][]string{
			{"11", "12"},
			{"21", "22"},
		},
		b: []string{"1", "2"},
	}

	a2 := a1
	a1.a[0][0] = "changed"
	a1.b[0] = "changed"

	copy(a2.a, a1.a)
	copy(a2.b, a1.b)
	a1.a[0][0] = "changed2"
	a1.b[0] = "changed2"

	a2.a = make([][]string, len(a2.a))
	a2.b = make([]string, len(a2.b))
	copy(a2.a, a1.a)
	copy(a2.b, a1.b)
	a1.a[0][0] = "changed3"
	a1.b[0] = "changed3"

	fmt.Println(a1)
	fmt.Println(a2)
}
