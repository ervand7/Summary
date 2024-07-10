package main

import (
	"fmt"
	"time"
)

/*
Даже несмотря на то, что есть Sleep и нет записи в канал, у нас не будет никакой
ошибки, так как нет wg group.
*/

func main() {
	ch := make(chan int)
	go func() {
		val := <-ch
		fmt.Println(val)
	}()

	time.Sleep(time.Second)
}
