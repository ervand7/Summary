package main

import (
	"fmt"
	"sync"
)

// panic: sync: negative WaitGroup counter

func main() {
	var wg sync.WaitGroup
	wg.Done()

	wg.Wait()

	fmt.Println("Hello")
}
