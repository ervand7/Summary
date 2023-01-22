package main

import "fmt"

// cap is 5 because we cut the first elem from a when we declare b

func main() {
	a := make([]int, 6, 6)
	for i := 0; i < len(a); i++ {
		a[i] = i
	}

	b := a[1:3]
	fmt.Println(len(b), cap(b)) // 2 5
}
