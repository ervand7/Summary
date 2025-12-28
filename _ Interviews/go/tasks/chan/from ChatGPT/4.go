package main

import (
	"fmt"
	"time"
)

// we will be stuck in cycle because we can endlessly read default data
// from closed channel
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
