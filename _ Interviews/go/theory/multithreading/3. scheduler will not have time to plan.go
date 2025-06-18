package main

import (
	"fmt"
)

// Nothing will be displayed because the planner will not have time to plan goroutines.
// We need to use sync.WaitGroup or sleep

func main() {
	for i := 0; i < 10; i++ {
		go func(item int) {
			fmt.Println(item)
		}(i)
	}
}
