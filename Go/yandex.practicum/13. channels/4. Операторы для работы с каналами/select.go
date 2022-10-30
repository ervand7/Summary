package main

/*
Изучите синтаксис:
select {
case x := <-ch1:
    // сценарий выполнится, если быстрее всего новое значение окажется в канале ch1
case y := <-ch2:
    // сценарий выполнится, если быстрее всего новое значение окажется в канале ch2
case ch3 <- z:
    // сценарий выполнится, если быстрее отправим значение в канал ch3
default:
    // код выполнится, если не подошёл ни один из вариантов выше
}
*/

import (
	"bytes"
	"fmt"
	"runtime/debug"
)

func Fibonacci(ch chan int, quit chan bool) {
	// эти 2 строчки для того, чтобы понять, в какой горутине мы находимся
	gr := bytes.Fields(debug.Stack())[1]
	fmt.Println("===========main", string(gr))

	x, y := 0, 1
loop: // метка цикла
	for {
		select {
		// записываем x в канал. Тут горутина заблокируется до тех пор, пока
		// в функции main это значение не прочтется
		case ch <- x:
			x, y = y, x+y
		case <-quit: // параллельно ждём сигнала об окончании работы
			break loop
		}
	}
}

func main() {
	ch := make(chan int)
	quit := make(chan bool)

	go func() {
		// эти 2 строчки для того, чтобы понять, в какой горутине мы находимся
		gr := bytes.Fields(debug.Stack())[1]
		fmt.Println("===========anon", string(gr))

		for i := 0; i < 15; i++ {
			fmt.Println(<-ch)
		}
		// подаём сигнал об окончании работы
		quit <- true
	}()

	// эти 2 строчки для того, чтобы понять, в какой горутине мы находимся
	gr := bytes.Fields(debug.Stack())[1]
	fmt.Println("===========main", string(gr))
	
	Fibonacci(ch, quit)
}
