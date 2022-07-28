package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	// 2021-07-14 22:28:51.947371 +0300 MSK

	loc, _ := time.LoadLocation("Europe/Berlin")
	// Здесь конструкция now.In(loc) приводит время к нужному часовому поясу
	fmt.Println(now.In(loc))
	// 2021-07-14 20:28:51.947371 +0100 CET
}
