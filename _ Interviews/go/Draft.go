package main

import (
	"fmt"
	"sync"
)

const workersCount = 10

// fanOut разбивает входящий канал на слайс с кол-вом `n` каналов.
// В дальнейшем `n` - будет кол-во воркеров, обрабатывающих данные.
// Значения из входного канала складываются в подканалы по принципу round-robin
func fanOut(inputCh chan int, n int) []chan int {
	result := make([]chan int, 0, n)
	for i := 0; i < n; i++ {
		ch := make(chan int)
		result = append(result, ch)
	}

	go func() {
		defer func(result []chan int) {
			for _, ch := range result {
				// эта горутина есть писатель по отношению к горутине Work
				// которая читает каждый из каналов через for-range
				close(ch)
			}
		}(result)

		for i := 0; ; i++ {
			if i == len(result) {
				i = 0
			}

			value, ok := <-inputCh
			if !ok {
				return
			}

			result[i] <- value
		}
	}()

	return result
}

// fanIn принимает много маленьких каналов, которые предоставил воркер
// и склеивает эти каналы в один результирующий
func fanIn(inputChs ...chan int) chan int {
	result := make(chan int)

	go func() {
		wg := &sync.WaitGroup{}
		for _, inputCh := range inputChs {
			wg.Add(1)

			go func(inputCh chan int) {
				defer wg.Done()
				for val := range inputCh {
					result <- val
				}
			}(inputCh)
		}

		wg.Wait()
		// писатель (горутина fanIn) закрывает канал, в который записывал
		close(result)
	}()

	return result
}

// Work совершает какую-то работу. В данном примере в холостую прибавляет 0.
// Для чего нужен воркер в данном паттерне? Для того, чтобы после того, как
// мы разбили большой канал на маленькие, взять и одновременно запустить
// много воркеров. Предварительно передав каждому воркеру по маленькому каналу.
func Work(input, out chan int) {
	for num := range input {
		out <- num + 0
	}

	// писатель (горутина Worker) закрывает канал, в который записывал
	close(out)
}

func main() {
	inputCh := make(chan int)

	// генерируем входные значения и кладём в inputCh
	go func() {
		for i := 0; i < 100; i++ {
			inputCh <- i
		}

		// данная горутина является писателем и закрывает этот канал, так как
		// читатель (fanOut) читает через for-range
		close(inputCh)
	}()

	// здесь fanOut
	fanOutChs := fanOut(inputCh, workersCount)
	workerChs := make([]chan int, 0, workersCount)
	for _, fanOutCh := range fanOutChs {
		workerCh := make(chan int)
		go Work(fanOutCh, workerCh)
		workerChs = append(workerChs, workerCh)
	}

	// здесь fanIn
	for v := range fanIn(workerChs...) {
		fmt.Println(v)
	}
}
