package main

import (
	"fmt"
	"sync"
)

/*
Словим deadlock так как мы будем заблокированы в for-range и defer wg.Done()
не отработает.

Данный пример изначально написан неправильно. Нам вообще wg тут не нужен будет
если канал сделать небуфф.
*/

func main() {
	ch := make(chan int, 10)

	var wg sync.WaitGroup
	wg.Add(1)
	go func() {
		defer wg.Done()
		for v := range ch {
			fmt.Println(v)
		}
	}()

	for i := 0; i < 5; i++ {
		ch <- i
	}

	wg.Wait()
}

/*
0
1
2
3
4
fatal error: all goroutines are asleep - deadlock!
*/
