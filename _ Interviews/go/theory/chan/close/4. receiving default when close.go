package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan bool)
	go func() {
		val := <-ch
		fmt.Println(val)
		return
	}()

	close(ch)
	time.Sleep(time.Second)
}
