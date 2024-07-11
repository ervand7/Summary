package main

import (
	"fmt"
	"time"
)

/*
То же самое касается и не до конца заполненного буфф канала
*/

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
