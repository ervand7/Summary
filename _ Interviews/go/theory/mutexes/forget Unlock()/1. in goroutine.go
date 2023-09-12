package main

import (
	"fmt"
	"sync"
	"time"
)

/*
Если забыть сделать Unlock(), то fmt.Println(x) исполнится только 1 раз
*/

func main() {
	var x int
	mux := sync.Mutex{}
	for i := 0; i < 10; i++ {
		go func() {
			mux.Lock()
			x += 1
			fmt.Println(x)
			// mux.Unlock() // забыли разлочить
		}()
	}

	time.Sleep(time.Second)
}
