package main

import (
	"fmt"
	"runtime"
)

/*
Без примитивов синхронизации результат никогда не будет 999
runtime.GOMAXPROCS(1) увеличит шансы на то, что ни одна из горутин не отработает.
*/

var num int

func main() {
	runtime.GOMAXPROCS(1)
	for i := range 1000 {
		go func(item int) {
			num = item
		}(i)
	}
	fmt.Printf("num is %d", num)
}
