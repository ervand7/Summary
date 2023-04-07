package main

import (
	"fmt"
	"sync"
	"time"
)

/*
Блокировка мьютексом - это не глобальная блокировка
*/

var a int

func main() {
	mux := sync.Mutex{}
	for i := 0; i < 10; i++ {
		go func() {
			mux.Lock()
			a += 1
			// mux.Unlock() // забыли разлочить
		}()
	}

	for i := 0; i < 10; i++ {
		go func() {
			a += 1
		}()
	}

	time.Sleep(time.Second)
	fmt.Println(a) // 11
}
