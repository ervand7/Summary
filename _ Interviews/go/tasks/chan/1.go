package main

import (
	"fmt"
	"sync"
)

/*
Принтом выведется только одно число, а потом будет
fatal error: all goroutines are asleep - deadlock!
Так как у нас только 1 раз вычитывается значение, а записывается больше 1 раза
*/

func main() {
	ch := make(chan int)
	wg := &sync.WaitGroup{}
	wg.Add(3)
	for i := 0; i < 3; i++ {
		go func(idx int, wg *sync.WaitGroup) {
			ch <- (idx + 1) * 2
			wg.Done()
		}(i, wg)
	}
	fmt.Printf("result: %d\n", <-ch)
	wg.Wait() // если закомментировать Wait, то ошибки не будет
}
