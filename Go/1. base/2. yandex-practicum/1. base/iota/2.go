package main

import "fmt"

const (
	_ = iota * 10 // обратите внимание, что можно пропускать константы
	ten
	hundred
	thousand
)

const (
	hello = "Hello, world!" // iota равна 0
	one   = 1               // iota равна 1

	black = iota // iota равна 2
	gray
)

func main() {
	fmt.Println(ten, hundred, thousand)  // 10 20 30
	fmt.Println(hello, one, black, gray) // Hello, world! 1 2 3
}
