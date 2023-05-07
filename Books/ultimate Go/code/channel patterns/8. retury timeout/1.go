package main

import (
	"context"
	"errors"
	"fmt"
	"time"
)

/*
Паттерн применяется, если мы хотим делать ping, например к БД и не хотим
сразу фейлиться. Хотим иметь какое-то кол-во попыток.
*/

func retryTimeout(
	ctx context.Context,
	retryInterval time.Duration,
	check func(ctx context.Context) error,
) {
	for {
		fmt.Println("perform user check call")
		if err := check(ctx); err == nil {
			fmt.Println("work finished successfully")
			return
		}
		if ctx.Err() != nil {
			fmt.Println("time expired 1 :", ctx.Err())
			return
		}
		fmt.Printf("wait %s before trying again\n", retryInterval)
		t := time.NewTimer(retryInterval)
		select {
		case <-ctx.Done():
			fmt.Println("timed expired 2 :", ctx.Err())
			t.Stop()
			return
		case <-t.C:
			fmt.Println("retry again")
		}
	}
}

func main() {
	// сэмитируем работу check-функции, как будто база всегда не отвечает
	var f = func(ctx context.Context) error {
		return errors.New("db is not alive")
	}
	ctx, cancel := context.WithTimeout(context.Background(), time.Second*3)
	defer cancel()
	retryInterval := time.Second

	retryTimeout(ctx, retryInterval, f)
}
