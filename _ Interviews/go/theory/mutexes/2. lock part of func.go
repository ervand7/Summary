package main

import (
	"fmt"
	"sync"
	"time"
)

/*
Можно залочить мьютексом только часть функции:
time.Sleep(time.Millisecond) будет выполняться горутинами одновременно.

Тут важный момент: мы передаем ссылку на мьютекс. Иначе он будет бесполезен
и у нас возникнет data race.
*/

const numRequests = 10000

var count int

func networkRequest(mux *sync.Mutex) {
	time.Sleep(time.Second) // Эмуляция сетевого запроса.
	mux.Lock()
	count++
	mux.Unlock()
}

func main() {
	mux := sync.Mutex{}
	wg := sync.WaitGroup{}
	for i := 0; i < numRequests; i++ {
		wg.Add(1)
		go func() {
			networkRequest(&mux)
			wg.Done()
		}()
	}

	wg.Wait()
	fmt.Println(count) // 10000
}
