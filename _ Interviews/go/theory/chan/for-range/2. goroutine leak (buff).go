package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int, 100)
	go func() {
		for v := range ch {
			fmt.Println(v)
		}
	}()

	for i := 0; i < 10; i++ {
		ch <- i
	}

	time.Sleep(time.Second)
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
