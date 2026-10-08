package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan string)

	go func() {
		time.Sleep(100 * time.Millisecond)
		close(ch)
	}()

	for {
		select {
		case msg, ok := <-ch:
			fmt.Println("received:", msg, "ok=", ok)
			time.Sleep(50 * time.Millisecond)
		default:
			fmt.Println("default branch")
			time.Sleep(20 * time.Millisecond)
		}
	}
}
