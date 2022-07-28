package main

import (
	"fmt"
	"log"
	"time"
)

/*
Оказалось, что один из сторонних сервисов, взаимодействующих
с вашим, передаёт время в своём формате, в виде строки.
Задача — достать объект типа Time из строки 2021-09-19T15:59:41+03:00:
*/

func main() {
	currentTimeStr := "2021-09-19T15:59:41+03:00"
	layout := time.RFC3339
	currentTime, err := time.Parse(layout, currentTimeStr)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(currentTime) // 2021-09-19 15:59:41 +0300 MSK
}
