package main

import (
	"fmt"
	"sync"
	"time"
)

/*
В данном примере много горутин будут читать из одного канала. Как только
Пока в канал ничего не будет поступать, будет принтится блок default. А после закрытия
канала все горутины получат нулевое значение канала.
*/

var ch = make(chan struct{})

func thread(wg *sync.WaitGroup, i int) {
	for {
		select {
		// после закрытия канала получаем нулевое значение
		case <-ch:
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
	for i := 0; i < 10; i++ {
		wg.Add(1)
		go thread(&wg, i)
	}
	time.Sleep(1 * time.Second)

	// close(ch)
	wg.Wait()
}
