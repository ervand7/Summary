package main

import (
	"fmt"
	"sync"
)

/*
Данный пример содержит data race. И из-за малого n он постоянно выводит 4.
Однако, если раскомментировать log.Println("logging"),
то будем получать 2.

Почему так происходит?
log.Println("logging") каждый раз заставляет планировщик делать
Context switch, и связка read-modify-write уже не работает непрерывно.
*/

var counter int

func main() {
	const grs = 2
	var wg sync.WaitGroup
	wg.Add(grs)
	for g := 0; g < grs; g++ {
		go func() {
			for i := 0; i < 2; i++ {
				value := counter
				value++
				// log.Println("logging")
				counter = value
			}
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println("Counter:", counter)
}
