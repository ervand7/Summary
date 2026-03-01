package main

import (
	"fmt"
	"sync"
	"time"
)

/*
В данном примере много горутин будут пытаться прочесть из одного канала.
Пока в канал ничего не будет поступать, будет отрабатывать блок default. А после закрытия
канала все горутины получат нулевое значение канала.
*/

var channel = make(chan struct{})

func worker(wg *sync.WaitGroup, id int) {
	for {
		select {
		// после закрытия канала получаем нулевое значение
		case <-channel:
			fmt.Println("Завершаем", id)
			wg.Done()
			return
		default:
			fmt.Println(id)
		}
		time.Sleep(50 * time.Millisecond)
	}
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go worker(&wg, i)
	}
	time.Sleep(1 * time.Second)

	close(channel)
	wg.Wait()
}
