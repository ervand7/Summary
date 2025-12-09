package main

import "fmt"

func main() {
	a := []int{1, 2, 3}
	b := a
	c := b[:1]
	d := b[1:]

	d[0] = 9999999
	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c[:3])
	fmt.Println(d)
}
