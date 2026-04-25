package main

import "fmt"

// Split work into stages, each stage runs in its own goroutine and passes data via
// channels.

// stage 1: generate numbers
func gen() <-chan int {
	out := make(chan int)
	go func() {
		for i := 1; i <= 3; i++ {
			out <- i
		}
		close(out)
	}()
	return out
}

// stage 2: square numbers
func square(in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		for v := range in {
			out <- v * v
		}
		close(out)
	}()
	return out
}

func main() {
	for v := range square(gen()) {
		fmt.Println(v) // 1, 4, 9
	}
}
