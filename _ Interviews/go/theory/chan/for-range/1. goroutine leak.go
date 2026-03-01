package main

import (
	"fmt"
)

func main() {
	ch := make(chan int)
	go func() {
		for v := range ch {
			fmt.Println(v)
		}
	}()

	for i := 0; i < 10; i++ {
		ch <- i
	}
}

/*
0
1
2
3
4
5
6
7
8
9
*/
