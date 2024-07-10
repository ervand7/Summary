package main

import (
	"fmt"
	"sync"
	"time"
)

/*
Задание: сделать так, чтобы у нас одновременно работало только 10 горутин.
Для этого мы можем использовать буферизированный канал с размером буфера 10.
*/

func main() {
	wg := sync.WaitGroup{}
	ch := make(chan bool, 10)

	for i := 0; i < 100; i++ {
		ch <- true
		wg.Add(1)

		go func(n int) {
			defer wg.Done()

			time.Sleep(time.Second)
			fmt.Println("do something concurrently", n)
			<-ch
		}(i)
	}

	wg.Wait()
	fmt.Println("do something in the end")
}
