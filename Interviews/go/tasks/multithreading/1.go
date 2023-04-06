package main

import (
	"fmt"
)

/*
Мораль: без примитивов синхронизации результат никогда не будет 999
И что-то обещанный runtime.GOMAXPROCS(1) тоже не поможет
*/

var num int

func main() {
	for i := 0; i < 1000; i++ {
		go func(item int) {
			num = item
		}(i)
	}
	fmt.Printf("num is %d", num)
}
