package main

import (
	"fmt"
	"runtime"
	"sync"
)

/*
Есть 10 единиц работы и 8 работающих одновременно горутин. Кто-то из
горутин сделает больше работы, кто-то меньше. В любом случае это
будет выполнено неравномерно.
*/

func main() {
	capacity := 100
	work := make([]string, 0, capacity)
	for i := 0; i < capacity; i++ {
		work = append(work, "paper")
	}

	g := runtime.GOMAXPROCS(0)
	var wg sync.WaitGroup
	wg.Add(g)
	ch := make(chan string, g)

	for i := 0; i < g; i++ {
		go func(i int) {
			defer wg.Done()
			for wrk := range ch {
				fmt.Printf("child %d : recv'd signal : %s\n", i, wrk)
			}
			fmt.Printf("child %d : recv'd shutdown signal\n", i)
		}(i)
	}
	for _, wrk := range work {
		ch <- wrk
	}
	close(ch)
	wg.Wait()
}
