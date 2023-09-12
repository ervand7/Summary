package main

import (
	"fmt"
	"runtime"
	"time"
)

// GOMAXPROCS restricts number of CPU that can be used simultaneously.
// This program will be single threaded and have a single P/M to execute
// all Goroutines. The function is capitalized because it’s also an
// environment variable. Though this function call will overwrite the variable.

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
