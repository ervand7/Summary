package main

import (
	"fmt"
	"time"
)

// because panic happened in the child goroutine, and each goroutine has its
// own panic/recover chain.

func main() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in main goroutine in f", r)
		}
	}()

	go parent()

	time.Sleep(1 * time.Second)
}

func parent() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("Recovered in parent goroutine in f", r)
		}
	}()

	go child()
}

func child() {
	panic("boom")
}
