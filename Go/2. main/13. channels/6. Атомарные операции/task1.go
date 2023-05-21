package main

/*
Перед вами код, в котором горутины увеличивают значение счётчика.
Чаще всего программа выводит неверный результат. Исправьте код так,
чтобы значение счётчика было правильным.
*/

import (
	"fmt"
	"sync"
	"sync/atomic"
)

var counter int64

func thread(wg *sync.WaitGroup) {
	for i := 0; i < 10000; i++ {
		atomic.AddInt64(&counter, 1)
	}
	wg.Done()
}

func main() {
	var wg sync.WaitGroup
	for i := 0; i < 20; i++ {
		wg.Add(1)
		go thread(&wg)
	}
	wg.Wait()
	// программа должна выводить 200000
	fmt.Println(counter)
}
