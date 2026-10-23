package main

import (
	"fmt"
	"time"
)

// Debounce: execute only after events stop coming.
// Без Debounce: 6 запросов к серверу (G, Go, Gol и т. д.).
// С Debounce: 1 запрос (Golang), когда пользователь перестал печатать на 500 мс.

func main() {
	var timer *time.Timer

	search := func(query string) {
		if timer != nil {
			timer.Stop() // cancel previous scheduled call
		}

		timer = time.AfterFunc(500*time.Millisecond, func() {
			fmt.Println("Searching:", query)
		})
	}

	search("G")
	search("Go")
	search("Gol")
	search("Golang")

	time.Sleep(time.Second)
}
