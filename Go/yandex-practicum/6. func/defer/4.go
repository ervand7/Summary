package main

import (
	"fmt"
	"time"
)

func metricTime(start time.Time) {
	fmt.Println(time.Now().Sub(start))
}

func VeryLongTimeFunction() {
	defer metricTime(time.Now())
	time.Sleep(1 * time.Second)
}

func main() {
	VeryLongTimeFunction() // 1.001064583s
}
