package main

import "fmt"

func push(a []int) {
	a = append(a, a[len(a)-1]+1)
}

func main() {
	x := []int{5, 6, 7}
	push(x[:1])
	push(x)
	fmt.Println(x)
}
