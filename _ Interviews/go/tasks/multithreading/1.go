package main

import (
	"fmt"
	"runtime"
)

/*
Мораль: без примитивов синхронизации результат никогда не будет 999
runtime.GOMAXPROCS(1) увеличит шансы на то, что ни одна из горутин не отработает.
*/

var num int

func main() {
	runtime.GOMAXPROCS(1)
	for i := 0; i < 1000; i++ {
		go func(item int) {
			num = item
		}(i)
	}
	fmt.Printf("num is %d", num)
}
