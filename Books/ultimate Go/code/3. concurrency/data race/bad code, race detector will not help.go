package main

import (
	"fmt"
	"sync"
)

/*
В одной функции не должно быть больше одной пары Lock/Unlock.
В данном примере даже race detector не сможет определить data race
*/

var Counter int

func main() {
	const grs = 2
	var wg sync.WaitGroup
	wg.Add(grs)
	var mu sync.Mutex
	for g := 0; g < grs; g++ {
		go func() {
			for i := 0; i < 2; i++ {
				var value int
				mu.Lock() // <-- Bad Use Of Mutex
				{
					value = Counter
				}
				mu.Unlock()
				value++
				mu.Lock() // <-- Bad Use Of Mutex
				{
					Counter = value
				}
				mu.Unlock()
			}
			wg.Done()
		}()
	}
	wg.Wait()
	fmt.Println("Counter:", Counter)
}
