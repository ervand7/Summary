package main

import "fmt"

// What will happen if we uncomment

func change(a []int) {
	// a = append(a, 6) // line1
	for i := 0; i < len(a); i++ {
		a[i] += 1
	}
	// a = append(a, 6) // line2
}

func main() {
	var a = []int{1, 2, 3, 4, 5}
	change(a)
	fmt.Println(a)
}
