package main

import (
	"fmt"
	"time"
)

func main() {
	timer := time.AfterFunc(500*time.Millisecond, func() {
		fmt.Println("Searching:")
	})
	_ = timer

	time.Sleep(time.Second)
}
