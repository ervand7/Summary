package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	wg.Done()

	wg.Wait()

	fmt.Println("Hello")
}
