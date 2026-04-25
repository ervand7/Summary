package main

import (
	"fmt"
	"time"
)

// Goal: if events come rapidly → execute only once after things calm down.

func main() {
	var timer *time.Timer

	trigger := func() {
		if timer != nil {
			timer.Stop() // cancel previous scheduled call
		}

		timer = time.AfterFunc(500*time.Millisecond, func() {
			fmt.Println("Executed once after calm period")
		})
	}

	// simulate rapid events
	for i := 0; i < 5; i++ {
		trigger()
		time.Sleep(100 * time.Millisecond)
	}

	time.Sleep(1 * time.Second)
}
