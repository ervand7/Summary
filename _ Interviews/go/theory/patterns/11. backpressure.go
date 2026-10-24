package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int, 5)

	// fast producer
	go func() {
		for i := range 20 {
			time.Sleep(time.Millisecond * 100)
			ch <- i
			fmt.Printf("produced %d\n", i)
		}
		close(ch)
	}()

	// slow consumer
	for val := range ch {
		fmt.Printf("consumed %d\n", val)
		time.Sleep(time.Millisecond * 500)
	}
}
