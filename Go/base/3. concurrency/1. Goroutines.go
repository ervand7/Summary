package main

import (
	"fmt"
	"time"
)

func f(n int) {
	for i := 0; i < 10; i++ {
		fmt.Println("process №", n, ": result", i)
		time.Sleep(time.Millisecond * 300)
	}
}

func main() {
	for i := 0; i < 10; i++ {
		go f(i)
	}
	var input string
	fmt.Scanln(&input)
}
