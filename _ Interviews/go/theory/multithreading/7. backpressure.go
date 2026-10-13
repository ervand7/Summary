package main

import (
	"fmt"
	"time"
)

func main() {
	jobs := make(chan int, 2) // small buffer → backpressure

	// consumer (slow)
	go func() {
		for range jobs {
			time.Sleep(1 * time.Second)
		}
	}()

	// producer (fast)
	for i := 0; i < 5; i++ {
		jobs <- i
		fmt.Println("sent", i)
	}
	close(jobs)
}
