package main

import (
	"fmt"
	"runtime"
	"time"
)

// GOMAXPROCS restricts number of CPU that can be used simultaneously.
// Given program will run undefined time, then prints "finish".

func main() {
	runtime.GOMAXPROCS(1)
	go func() {
		for true {
			fmt.Println("Infinite loop")
		}
	}()

	time.Sleep(time.Millisecond)
	fmt.Println("finish")
}
