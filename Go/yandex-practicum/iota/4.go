package main

import "fmt"

const (
	one_ = 1 + iota*2
	three
	five
	seven
	nine
	eleven
)

func main() {
	fmt.Println(one_, three, five, seven, nine, eleven) // 1 3 5 7 9 11
}
