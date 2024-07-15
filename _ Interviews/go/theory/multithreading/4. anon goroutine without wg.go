package main

import (
	"fmt"
	"time"
)

/*
Даже несмотря на то, что есть Sleep и нет записи в канал, у нас не будет никакой ошибки.
*/

func main() {
	ch := make(chan int)
	for i := 0; i < 10; i++ {
		go func(num int) {
			fmt.Printf("goroutine %d waits...\n", num)
			val := <-ch
			fmt.Println(val)
		}(i)
	}

	time.Sleep(time.Second)
	fmt.Println("Ok")
}
