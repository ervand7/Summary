package main

import (
	"fmt"
	"time"
)

func mul(c chan int) {
	for i := 0; i < 3; i++ {
		num := <-c
		fmt.Println(num * num)
	}
}

func main() {
	fmt.Println("main() started")
	c := make(chan int, 3)

	go mul(c)

	c <- 1
	c <- 2
	c <- 3
	c <- 4 // тут main горутина заморозится
	c <- 5
	c <- 6
	c <- 7 // только тут будет deadlock

	time.Sleep(time.Second)
	fmt.Println("main() stopped")
}
