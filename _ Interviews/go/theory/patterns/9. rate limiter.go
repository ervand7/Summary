package main

import (
	"fmt"
	"time"
)

func main() {
	var (
		limit   = 5
		limiter = make(chan struct{}, limit)
	)

	// allow initial spike
	for range limit {
		limiter <- struct{}{}
	}

	// refill tokens every 500ms
	go func() {
		ticker := time.NewTicker(time.Millisecond * 500)
		defer ticker.Stop()

		for range ticker.C {
			select {
			case limiter <- struct{}{}: // added token
			default: // channel full → skip (no overflow)
			}
		}
	}()

	// simulate requests
	for i := range 10 {
		<-limiter // acquire token

		fmt.Println("request", i, time.Now().Format("15:04:05.000"))
	}
}
