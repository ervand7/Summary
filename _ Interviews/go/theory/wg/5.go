package main

import (
	"fmt"
	"sync"
)

// panic: sync: negative WaitGroup counter

func main() {
	var wg sync.WaitGroup

	wg.Done()

	fmt.Println("Hello")
}
