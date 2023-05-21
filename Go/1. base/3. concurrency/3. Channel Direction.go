package main

import (
	"fmt"
	"time"
)

// Now c can only be sent to
func pinger_(c chan<- string) {
	for i := 0; ; i++ {
		c <- "ping"
	}
}

func ponger_(c chan string) {
	for i := 0; ; i++ {
		c <- "pong"
	}
}

// Now c can only be received
func printer_(c <-chan string) {
	for {
		msg := <-c
		fmt.Println(msg)
		time.Sleep(time.Second * 1)
	}
}

func main() {
	var ervand chan string = make(chan string)

	go pinger_(ervand)
	go ponger_(ervand)
	go printer_(ervand)

	var input string

	fmt.Scanln(&input)
}
