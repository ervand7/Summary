package main

import "fmt"

/*
Вывод будет 135790. Потому что при `for _ = range ch` вычитывается значение
из канала, а также при `case i := <-ch:`. Последнее значение (0) будет
уже считано из закрытого канала.
*/

func main() {
	ch := make(chan int)

	go func() {
		for i := 0; i < 11; i++ {
			ch <- i
		}
		close(ch)
	}()
	for _ = range ch {
		select {
		case i := <-ch:
			fmt.Println(i)
		}
	}
}
