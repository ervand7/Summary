package main

import (
	"fmt"
	"time"
)

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
