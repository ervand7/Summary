package main

import "fmt"

/*
Это отличный пример, чтобы посмотреть в дебаггере, как работает буффер
(если канал сделать буфферизированным) и как работает программа с
небуфферизированным каналом
*/

func fibonacci(n int, ch chan int) {
	x, y := 0, 1
	for i := 0; i < n; i++ {
		fmt.Println("=============1  ", x)
		ch <- x
		x, y = y, x+y
	}

	close(ch)
}

func main() {
	ch := make(chan int, 10)
	go fibonacci(15, ch)

	for i := range ch {
		fmt.Printf("%d ", i)
		fmt.Println("=============2")
	}
}
