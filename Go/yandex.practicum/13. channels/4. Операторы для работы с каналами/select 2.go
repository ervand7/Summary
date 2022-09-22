package main

import (
	"fmt"
	"sync"
	"time"
)

var done = make(chan struct{})

func thread(wg *sync.WaitGroup, i int) {
	for {
		select {
		case <-done:
			fmt.Println("Завершаем", i)
			wg.Done()
			return
		default:
			fmt.Println(i)
		}
		time.Sleep(50 * time.Millisecond)
	}
}

func main() {
	var wg sync.WaitGroup

	// создаём горутины
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go thread(&wg, i)
	}
	time.Sleep(2 * time.Second)
	// сообщаем горутинам о завершении работы
	close(done)
	// ждём завершения всех горутин
	wg.Wait()
}
