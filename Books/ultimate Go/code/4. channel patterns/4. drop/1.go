package main

import (
	"fmt"
	"time"
)

/*
Смысл паттерна: при превышении лимита неких запросов, когда кол-во
работы больше, чем предельная пропускная способность, мы можем отклонять
те запросы, которые мы не в силе (не успеваем) обработать.

В данном примере есть буф канал, с capacity = 5. И есть писатель, который
пишет в канал больше 5 раз (20 раз). Когда канал переполняется, он блокируется,
пока из него не будет вычитано хотя бы одно значение. И в этот момент
горутина-писатель ничего не может в него записать и срабатывает default -
как раз та ситуация, где мы превысили лимит возможностей.
*/

const capacity = 5
const work = 20

func main() {
	ch := make(chan int, capacity)
	go func() {
		for p := range ch {
			fmt.Println("child : recv'd signal :", p)
		}
	}()

	for w := 0; w < work; w++ {
		select {
		case ch <- w:
			fmt.Println("parent : sent signal :", w)
		default:
			fmt.Println("parent : dropped data :", w)
		}
	}
	close(ch)
	fmt.Println("parent : sent shutdown signal")
	time.Sleep(time.Second)
	fmt.Println("-------------------------------------------------")
}
