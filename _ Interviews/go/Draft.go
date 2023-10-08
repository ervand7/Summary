package main

import (
	"fmt"
	"time"
)

func main() {
	go func() {
		for i := 0; i < 5000; i++ {
			fmt.Println("Goroutine 1:", i)
		}
	}()

	go func() {
		for i := 0; i < 5000; i++ {
			fmt.Println("Goroutine 2:", i)
		}
	}()

	time.Sleep(time.Second)
}
