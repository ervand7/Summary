package main

import (
	"fmt"
)

func Print[L any, V fmt.Stringer](labels []L, vals []V) {
	for i, v := range vals {
		fmt.Println(labels[i], v.String())
	}
}

type ervand string

func (e ervand) String() string { return "Hello" }

func main() {
	var e ervand
	var e2 ervand
	Print([]int{1, 2}, []ervand{e, e2})
}

/*
	1 Hello
	2 Hello
*/
