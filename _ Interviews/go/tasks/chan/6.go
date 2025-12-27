package main

import (
	"fmt"
	"time"
)

func mul(ch chan int) {
	for i := 0; i < 3; i++ {
		num := <-ch
		fmt.Println(num * num)
	}
}

func main() {
	fmt.Println("main() started")
	ch := make(chan int, 3)

	go mul(ch)

	ch <- 1
	ch <- 2
	ch <- 3
	ch <- 4 // тут main горутина заморозится
	ch <- 5
	ch <- 6
	ch <- 7 // только тут будет deadlock

	time.Sleep(time.Second)
	fmt.Println("main() stopped")
}
