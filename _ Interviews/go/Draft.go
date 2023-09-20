package main

import (
	"fmt"
	"time"
)

func main() {
	// Get the current time
	currentTime := time.Now()

	// Calculate yesterday's time by subtracting 24 hours
	yesterday := currentTime.AddDate(0, 0, -1)

	// Set the time to 00:00:00.000000
	yesterdayStartOfDay := time.Date(yesterday.Year(), yesterday.Month(), yesterday.Day(), 0, 0, 0, 0, &time.Location{})

	fmt.Println("Yesterday's start of day:", yesterdayStartOfDay)
}
