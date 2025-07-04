package main

import (
	"fmt"
)

/*
Мы не увидим ничего, так как горутина-читатель не успеет запланироваться, а
горутина-писатель не заблокируется, так как канал буферизированный
*/

func main() {
	ch := make(chan int, 10)
	go func() {
		for v := range ch {
			fmt.Println(v)
		}
	}()

	for i := 0; i < 5; i++ {
		ch <- i
	}
}
