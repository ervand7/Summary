package main

import "fmt"

type Weekday int

const (
	Monday Weekday = iota + 1
	Tuesday
	Wednesday
	Thursday
	Friday
	Saturday
	Sunday
)

func NextDay(day Weekday) Weekday {
	result := (day % 7) + 1
	return result
}

func main() {
	var today Weekday = Friday
	tomorrow := NextDay(today)
	fmt.Println("today =", today, "tomorrow =", tomorrow)
	// today = 7 tomorrow = 1
}
