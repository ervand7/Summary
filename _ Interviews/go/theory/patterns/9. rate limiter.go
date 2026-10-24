package main

import (
	"fmt"
	"time"
)

func main() {
	limit := 5
	limiter := make(chan struct{}, limit) // burst capacity = 5

	// fill initial tokens (allow burst at start)
	for range limit {
		limiter <- struct{}{}
	}

	// refill tokens every 500ms
	go func() {
		ticker := time.NewTicker(500 * time.Millisecond)
		defer ticker.Stop()

		for range ticker.C {
			select {
			case limiter <- struct{}{}:
				// added token
			default:
				// channel full → skip (no overflow)
			}
		}
	}()

	// simulate requests
	for i := range 10 {
		<-limiter // acquire token

		fmt.Println("request", i, time.Now().Format("15:04:05.000"))
	}
}
