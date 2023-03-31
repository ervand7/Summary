package main

import (
	"fmt"
	"sync"
)

/*
Задание: сделать так, чтобы у нас одновременно работало только 10 горутин.
Для этого мы можем использовать буферизированный канал с размером буфера 10.
*/

func main() {
	wg := sync.WaitGroup{}
	q := make(chan bool, 10)

	for i := 0; i < 100; i++ {
		q <- true
		wg.Add(1)

		go func(n int) {
			fmt.Println("do something concurrently", n)
			<-q
			wg.Done()
		}(i)
	}

	wg.Wait()
	fmt.Println("do something in the end")
}
