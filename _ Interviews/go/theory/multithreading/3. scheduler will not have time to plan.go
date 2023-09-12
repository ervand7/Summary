package main

import (
	"fmt"
)

// nothing will be displayed, because planner will not have time to plan goroutines.
// We need to use sync.WaitGroup or sleep

func main() {
	for i := 0; i < 10; i++ {
		go func(item int) {
			fmt.Println(item)
		}(i)
	}
}
