package main

import (
	"fmt"
	"time"
)

func main() {
	for i := 0; i < 1_000_000; i++ {
		go func() {
			fmt.Println(i)
		}()
	}

	time.Sleep(time.Second * 1)
}
