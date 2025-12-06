package main

import (
	"fmt"
	"time"
)

/*
Поскольку хотя бы 1 горутина (в данном случае анонимная) не заблокирована, то
дедлока не будет
*/

func main() {
	ch := make(chan int)
	go func() {
		for {
			fmt.Println("Hello")
		}
	}()

	val := <-ch
	fmt.Println(val)
	time.Sleep(time.Second * 5)
	fmt.Println("Ok")
}
