package main

import (
	"fmt"
	"log"
	"sync"
)

func fanOut(inputCh chan int, n int) []chan int {
	chs := make([]chan int, 0, n)
	for i := 0; i < n; i++ {
		ch := make(chan int)
		chs = append(chs, ch)
	}

	go func() {
		defer func(chs []chan int) {
			for _, ch := range chs {
				close(ch)
			}
		}(chs)

		for i := 0; ; i++ {
			if i == len(chs) {
				i = 0
			}

			num, ok := <-inputCh
			if !ok {
				return
			}

			ch := chs[i]
			ch <- num
		}
	}()

	return chs
}

func newWorker(input, out chan int) {
	go func() {
		defer func() {
			if x := recover(); x != nil {
				newWorker(input, out)
				log.Printf("run time panic: %v", x)
			}
		}()

		for num := range input {
			out <- 100500 / (num - 1)
		}

		close(out)
	}()
}

func fanIn(inputChs ...chan int) chan int {
	outCh := make(chan int)

	go func() {
		wg := &sync.WaitGroup{}

		for _, inputCh := range inputChs {
			wg.Add(1)

			go func(inputCh chan int) {
				defer wg.Done()
				for item := range inputCh {
					outCh <- item
				}
			}(inputCh)
		}

		wg.Wait()
		close(outCh)
	}()

	return outCh
}

const workersCount = 10

func main() {
	inputCh := make(chan int)

	// генерируем входные значения и кладём в inputCh
	go func() {
		for i := 0; i < 100; i++ {
			for j := 0; j < 120; j++ {
				inputCh <- i * j
			}
		}

		close(inputCh)
	}()

	// здесь fanOut
	fanOutChs := fanOut(inputCh, workersCount)
	workerChs := make([]chan int, 0, workersCount)
	for _, fanOutCh := range fanOutChs {
		workerCh := make(chan int)
		newWorker(fanOutCh, workerCh)
		workerChs = append(workerChs, workerCh)
	}

	// здесь fanIn
	for v := range fanIn(workerChs...) {
		fmt.Println(v)
	}
}
