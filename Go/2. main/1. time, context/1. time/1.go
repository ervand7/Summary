package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	fmt.Println("Год:", now.Year())            // Год: 2022
	fmt.Println("Месяц:", now.Month())         // Месяц: July
	fmt.Println("Число:", now.Day())           // Число: 27
	fmt.Println("День недели:", now.Weekday()) // День недели: Wednesday
	hour, min, sec := now.Clock()
	fmt.Printf("Время: %d, %d, %d\n", hour, min, sec)        // Время: 21, 9, 25
	fmt.Println("Часовой пояс:", now.Location())             // Часовой пояс: Local
	fmt.Println("timestamp в секундах:", now.Unix())         // timestamp в секундах: 1658945365
	fmt.Println("timestamp в наносекундах:", now.UnixNano()) // timestamp в наносекундах: 1658945365871788000
}
