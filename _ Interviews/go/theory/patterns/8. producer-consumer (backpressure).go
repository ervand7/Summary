package main

import (
	"fmt"
	"time"
)

func main() {
	jobs := make(chan int, 2) // small buffer → backpressure

	// consumer (slow)
	go func() {
		for j := range jobs {
			time.Sleep(1 * time.Second)
			fmt.Println("processed", j)
		}
	}()

	// producer (fast)
	for i := 0; i < 5; i++ {
		fmt.Println("sending", i)
		jobs <- i // blocks when buffer is full
		fmt.Println("sent", i)
	}
	close(jobs)
}
