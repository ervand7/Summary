package main

import (
	"fmt"
	"sync"
)

/*
Программа выведет
2
0
4
5
3
1
7
8
6
fatal error: all goroutines are asleep - deadlock!
Так как после вывода всех чисел у нас Wait будет ждать горутины, которой нет
*/

func main() {
	var wg sync.WaitGroup

	n := 10
	wg.Add(n)
	for i := 0; i < n-1; i++ {
		go func(v int) {
			fmt.Println(v)
			wg.Done()
		}(i)
	}
	wg.Wait()
}
