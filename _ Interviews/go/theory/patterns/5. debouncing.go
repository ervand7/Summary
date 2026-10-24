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

	search := func(val string) {
		if timer != nil {
			timer.Stop()
		}

		timer = time.AfterFunc(time.Millisecond*500, func() {
			fmt.Printf("searching: %s", val)
		})
	}

	search("G")
	search("Go")
	search("Gol")
	search("Golang")

	time.Sleep(time.Second)
}
