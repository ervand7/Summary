package main

import (
	"fmt"
	"time"
)

// при закрытии канала в него поступает дефолтное значение

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

// false
