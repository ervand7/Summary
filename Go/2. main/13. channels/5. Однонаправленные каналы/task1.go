package main

import (
	"bytes"
	"fmt"
	"runtime/debug"
)

/*
Допишите программу так, чтобы горутина прочитала все числа из каналов a и b и
отправила их в канал c.
Канал для чтения выбирается оператором select случайным образом.
Программа должна вывести числа от 10 до 29 в произвольном порядке.
*/

func thread(dec int) <-chan int {
	ch := make(chan int)
	go func() {
		for i := 0; i < 10; i++ {
			// эти 2 строчки для того, чтобы понять, в какой горутине мы находимся
			gr := bytes.Fields(debug.Stack())[1]
			fmt.Println("===========thread", string(gr))

			ch <- dec*10 + i
		}
		close(ch)
	}()
	return ch
}

func main() {
	a := thread(1)
	b := thread(2)
	c := make(chan int)
	go func() {
		for a != nil || b != nil {
			// эти 2 строчки для того, чтобы понять, в какой горутине мы находимся
			gr := bytes.Fields(debug.Stack())[1]
			fmt.Println("===========anon", string(gr))

			select {
			case v, ok := <-a:
				if !ok {
					a = nil
					continue
				}
				c <- v
			case v, ok := <-b:
				if !ok {
					b = nil
					continue
				}
				c <- v
			}
		}
		close(c)
	}()
	for v := range c {
		fmt.Println(v)
	}
}
