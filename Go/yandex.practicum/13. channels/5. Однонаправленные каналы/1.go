package main

import (
	"fmt"
	"strings"
)

/*
Часто каналы передаются в аргументах функций.
Как правило, внутри функций каналы используются только для отправки
данных или только для получения.
Чтобы избежать ошибки при выборе канала, можно определить в
параметре функции однонаправленный тип:
	<-chan — только для получения данных;
	chan<- — только для отправки данных.
*/

// Generate отправляет в канал out односимвольные строки.
// В сигнатуре мы говорим, что ждем канал, который исключительно на запись в него
func Generate(out chan<- string) {
	for ch := 'a'; ch <= 'z'; ch++ {
		out <- string(ch)
	}
	close(out)
}

// Process читает строки из канала in, переводит их в верхний регистр
// и отправляет в канал out.
func Process(in <-chan string, out chan<- string) {
	for v := range in {
		out <- strings.ToUpper(v)
	}
	close(out)
}

func main() {
	lower := make(chan string)
	upper := make(chan string)
	go Generate(lower)
	go Process(lower, upper)

	// выводим строки из канала upper по мере получения
	for s := range upper {
		fmt.Print(s)
	}
	// ABCDEFGHIJKLMNOPQRSTUVWXYZ
}
