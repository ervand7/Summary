package main

import (
	"fmt"
	"time"
)

func main() {
	// burst capacity = 2
	limiter := make(chan struct{}, 2)

	// fill initial tokens (allow burst at start)
	for i := 0; i < cap(limiter); i++ {
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
	for i := 1; i <= 10; i++ {
		<-limiter // acquire token

		fmt.Println("request", i, time.Now().Format("15:04:05.000"))
	}
}
