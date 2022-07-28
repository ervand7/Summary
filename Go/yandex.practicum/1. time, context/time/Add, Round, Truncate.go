package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	fmt.Println(now)
	fmt.Println(now.Add(time.Second))          // добавить интервал к текущему времени
	fmt.Println(now.Round(time.Hour))          // округлить время до часа
	fmt.Println(now.Truncate(3 * time.Minute)) // обрезать время до третьей минуты
}

/*
2022-07-27 21:28:35.433138 +0300 MSK m=+0.000071251
2022-07-27 21:28:36.433138 +0300 MSK m=+1.000071251
2022-07-27 21:00:00 +0300 MSK
2022-07-27 21:27:00 +0300 MSK
*/
