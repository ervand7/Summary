package main

import (
	"fmt"
	"sync"
)

/*
Мораль: 2 горутины могут одновременно читать из одного канала через
конструкцию for-range. Однако из-за этой конструкции defer с wg.Done()
не сможет исполниться, так как происходит блокировка и мы не можем
выйти из горутины. Код упадет на wg.Wait(). Для решения этой проблемы
нужно закрыть канал перед wg.Wait().

Закрывать канал должен именно писатель.
*/

func longOp(i int) {
	fmt.Println(i * 2)
}

func main() {
	some := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}

	someChan := make(chan int)
	var wg sync.WaitGroup
	for i := 0; i < 2; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for x := range someChan {
				longOp(x)
			}
		}()
	}

	for _, s := range some {
		someChan <- s
	}

	wg.Wait()
	close(someChan)
}
