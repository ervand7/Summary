package store

import "fmt"

type Foo interface {
	Do(int) int
}

func Bar(f Foo) {
	fmt.Println()
}
