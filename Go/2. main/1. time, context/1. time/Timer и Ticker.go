package main

import (
	"fmt"
	"time"
)

/*
Пакет time содержит типы Timer и Ticker.
У обоих есть поле C — канал, через который можно получать
сигнал по истечении времени.

Запомните разницу между типами:
	Timer срабатывает один раз;
	Ticker будет срабатывать снова и снова до вызова метода Stop().
*/

func main() {
	start := time.Now()
	timer := time.NewTimer(2 * time.Second) // создаём таймер
	t := <-timer.C                          // ожидаем срабатывания таймера
	fmt.Println(t.Sub(start).Seconds())     // выводим разницу во времени
}
