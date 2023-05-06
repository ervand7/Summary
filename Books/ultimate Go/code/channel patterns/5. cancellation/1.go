package main

import (
	"context"
	"fmt"
	"time"
)

/*
Если вместо `duration - 10` пропишем просто `duration`, то
получим `work cancelled`.

Здесь есть тонкий момент, почему был использован буф канал:
дело в том, что дочерняя горутина (писатель) должна в любом случае
записать в канал то, что она хочет записать. Вне зависимости, может
ли родительская горутина-читатель принять данные или нет.
В противном случае, если бы у нас использовался небуф канал, то
горутина-читатель заблокировалась бы и произошла утечка памяти.
*/

const duration time.Duration = time.Millisecond * 150

func main() {

	ctx, cancel := context.WithTimeout(context.Background(), duration)
	defer cancel()

	ch := make(chan string, 1)
	go func() {
		time.Sleep(duration - 10*time.Millisecond)
		ch <- "data"
	}()

	select {
	case d := <-ch:
		fmt.Println("work complete", d)
	case <-ctx.Done():
		fmt.Println("work cancelled")
	}

	time.Sleep(time.Second)
	fmt.Println("-------------------------------------------------")
}
