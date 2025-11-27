package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup

	wg.Add(1)
	go func() {
		wg.Add(1)
		go func() {
			fmt.Println("inner")
			wg.Done()
		}()
		wg.Done()
	}()

	wg.Wait()
	fmt.Println("done")
}
