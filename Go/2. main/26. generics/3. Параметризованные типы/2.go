package main

import "fmt"

// Можно использовать параметризацию типов и при описании структур:

type Tree[T any] struct {
	Value    T
	Children []*Tree[T]
}

func main() {
	var tInt = Tree[int]{Value: 10,
		Children: []*Tree[int]{
			{Value: 20},
		}}
	var tString = Tree[string]{Value: "alex",
		Children: []*Tree[string]{
			{Value: "mike"},
			{Value: "alice"},
		}}
	fmt.Printf("%#v\n", tInt)
	fmt.Printf("%#v", tString)
}

/*
main.Tree[int]{Value:10, Children:[]*main.Tree[int]{(*main.Tree[int])(0x14000130000)}}
main.Tree[string]{Value:"alex", Children:[]*main.Tree[string]{(*main.Tree[string])(0x14000112180), (*main.Tree[string])(0x140001121b0)}}
*/
