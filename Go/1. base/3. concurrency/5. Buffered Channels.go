package main

import (
	"fmt"
	"time"
)

func _pinger(c chan string) {
	for i := 0; ; i++ {
		c <- "ping"
	}
}

func _ponger(c chan string) {
	for i := 0; ; i++ {
		c <- "pong"
	}
}

func _printer(c chan string) {
	for {
		msg := <-c
		fmt.Println(msg)
		time.Sleep(time.Second * 1)
	}
}

func main() {
	/*
		This creates a buffered channel with a capacity of 10.
		Normally channels are synchronous; both sides of the channel
		will wait until the other side is ready. A buffered channel
		is asynchronous; sending or receiving a message will not
		wait unless the channel is already full.
	*/
	var ervand chan string = make(chan string, 10)

	go _pinger(ervand)
	go _ponger(ervand)
	go _printer(ervand)

	var input string
	fmt.Scanln(&input)
}
