package main

import "fmt"

func mutate(a []int) {
	for i := range a {
		a[i] *= 10
	}
	a = append(a, 999)
}

func main() {
	x := []int{1, 2, 3}
	mutate(x[:2])
	fmt.Println(x)
}
