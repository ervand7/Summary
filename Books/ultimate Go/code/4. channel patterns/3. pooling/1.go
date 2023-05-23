package main

import (
	"fmt"
	"runtime"
	"time"
)

// Чем-то напоминает workerpool

const work = 100

func main() {
	ch := make(chan string)
	g := runtime.GOMAXPROCS(0)
	for c := 0; c < g; c++ {
		go func(child int) {
			for d := range ch {
				fmt.Printf("child %d : recv'd signal : %s\n", child, d)
			}
			fmt.Printf("child %d : recv'd shutdown signal\n", child)
		}(c)
	}

	for w := 0; w < work; w++ {
		ch <- "data"
		fmt.Println("parent : sent signal :", w)
	}
	close(ch)
	fmt.Println("parent : sent shutdown signal")
	time.Sleep(time.Second)
	fmt.Println("-------------------------------------------------")
}
