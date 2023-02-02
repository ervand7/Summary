package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	// не нужно использовать make, достаточно указать тип переменной sync.Map
	var m sync.Map

	for i := 1; i <= 10; i++ {
		go func(index int) {
			m.Store(index, index*index)
			v, _ := m.Load(index)
			fmt.Printf("%d*%[1]d = %v\n", index, v)
		}(i)
	}
	time.Sleep(time.Second)
}
