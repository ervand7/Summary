package main

import (
	"context"
	"fmt"
	"sync"
	"time"
)

func main() {
	in := make(chan int, 100)
	out := make(chan int, 100)

	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()

	// Генерация данных
	go func() {
		for i := 0; i < 100; i++ {
			in <- i
		}
		close(in)
	}()

	processInParallel(ctx, in, out, 5)

	// Чтение результатов
	for result := range out {
		fmt.Println("Processed:", result)
	}
}

func processInParallel(ctx context.Context, in <-chan int, out chan<- int, workers int) {
	// 1. Необходимо написать параллельную обработку в кол-ве горутин равном workers
	//    Получаем данные из канала in, над каждым элементом выполняем processData
	//    Передаем результат в out

	// 2. В дополнение к этому необходимо добавить получение контекста и его обработку

	var wg sync.WaitGroup
	wg.Add(workers)

	for i := 0; i < workers; i++ {
		go func() {
			defer wg.Done()
			for {
				select {
				case <-ctx.Done():
					return
				case data, ok := <-in:
					if !ok {
						return
					}
					result := processData(data)

					select {
					case <-ctx.Done():
						return
					case out <- result:
					}
				}
			}
		}()
	}

	// Закрываем out после завершения всех воркеров
	go func() {
		wg.Wait()
		close(out)
	}()
}

func processData(data int) int {
	time.Sleep(100 * time.Millisecond) // Эмуляция тяжёлой операции
	return data * 2
}
