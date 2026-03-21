package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(2)
	go func() {
		time.Sleep(50 * time.Millisecond)
		fmt.Println(1)
		wg.Done()
	}()
	wg.Add(-1)
	go func() {
		fmt.Println(2)
		wg.Done()
	}()
	wg.Wait()
	fmt.Print(3)
}
